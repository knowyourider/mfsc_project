$(document).ready(function() {

  // for action list to expand from recommendation in goal_detail.html
  $('.expander-trigger').click(function(){
    // console.log("got to trigger");
    // this works when in the a tag, and the hidden div immediately follows the a tag
    // $(this).toggleClass("expander-hidden");
    // this works when the a tag is inside of another element, in this case the li
    $(this).toggleClass("expander-hidden");
  });

  // ------- SEARCH SUBMIT ON CHECKBOX change ------

  // click on checkbox submits form
  $('input[type="checkbox"]').change(function(event){
    // each time a new box is checked we should reset to page 1
    // (if nothing else ther may not be a page 2 in new result)
    $('#search-form').find('[type=hidden][name=page]').val('1')
    $('#search-form').submit()   
  });

  // Hijack submission and re-route to AJAX
  // per: https://realpython.com/blog/python/django-and-ajax-form-submissions/
  $('#search-form').on('submit', function(event){
      event.preventDefault();
      // console.log("-------form submitted!");  // sanity check
      perform_search($('#search-form').serializeArray());
  });

  // AJAX for search results
  function perform_search(formData) {
    // console.log("---- create post is working!"); // sanity check
    //var formData = $("#search-form").serializeArray()
    $.ajax({
        url : "results/", // the endpoint
        type : "GET", // http method
        data : formData, // data sent with the post request 
        // handle a successful response
        success : function(json) {
            // console.log(json); // log the returned json to the console
            $('.wide-column').html(json)
            // scroll to top of results
            $('html,body').animate({
                scrollTop: $("#search-form").offset().top - 30},
                'slow');
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status ); // provide a bit more info about the error to the console
            $('.wide-column').html(xhr.responseText); 
        }
    });  };

  // ------- SEARCH ------
  // link to clear search
  $('#clear').click(function(event){
    // clear the value in the search field
    $('input[name="q"]').val('')
    // submit
    $('form[name="menu"]').submit()
    
  });

  // more checkboxes
  // class is attached to p, though click is on "a" tag
  $('.control-box--more').click(function(){
    // toggle the short-list class
    $(this).parent().find(".control-box--list").toggleClass("short-list");
    $(this).hide();
    // console.log("----- p:nth-child(4): " + $(this).parent().parent().find("p:nth-child(4)").html());
    // $(this).parent().parent().find("p:nth-child(4)").show();
    $(this).parent().find("p:nth-child(4)").show();
  });

  // fewer checkboxes
  $('.control-box--fewer').click(function(){
    $(this).parent().find(".control-box--list").toggleClass("short-list");
    $(this).hide(); // hide fewer
    $(this).parent().find("p:nth-child(3)").show(); // show more
    // scroll to top of search box(es?) on fewer
    $('html,body').animate({
        // scrollTop: $("#"+id).offset().top},
        scrollTop: $("#by-tag").offset().top - 50},
        'slow');
  });

  // ------- MENU PAGINATION ------

  // Turn page selection into form submit
  // q (and other?) parameters are in the form and will be submited? 
  // document.on syntax required since this the markup was loaded by ajax.
  $(document).on("click", "#paging", function(event){
    event.preventDefault();
    // get the page number from href
    var chosen_href = $(event.target).closest('li').children('a').attr('href');
    var href_split = chosen_href.split('=');  
    // page number = href_split[1]  
    // alert('in page nav. page num: ' + href_split[1]); 
    // set the page number in the hidden field
    $('#search-form').find('[type=hidden][name=page]').val(href_split[1])
    $('#search-form').submit()
  });


});	// end doc ready
