$(document).ready(function() {

  // ------- GOAL PAGE RECOMMENDATION DROPDOWN ------
  // for action list to expand from recommendation in goal_detail.html
  $('.expander-trigger').click(function(){
    // console.log("got to trigger");
    // this works when in the a tag, and the hidden div immediately follows the a tag
    // $(this).toggleClass("expander-hidden");
    // this works when the a tag is inside of another element, in this case the li
    $(this).toggleClass("expander-hidden");
  });

  
  // ---------- NAVIGATION ----------
  // This is happening on page load
  // Assign var menuToggle to stand for the element js-top-navigation-mobile-menu
  // and remove (unbind) any previous event handler
  var menuToggle = $('#js-top-navigation-mobile-menu').unbind();
  // Here, on page load, we're going to remove the class show
  // .. if we happen to be in mobile mode, this will make sure the menu 
  // isn't dropped down
  $('#js-top-navigation-menu').removeClass("show");
  
  // this adds click "listener" to the mobile MENU link
  menuToggle.on('click', function(e) {
    e.preventDefault();
    // toggle the primary mobile menu down (if it's up) and up (if already down)
    $('#js-top-navigation-menu').slideToggle(function(){
      // if css media query has hidden the full menu, then remove "full" style
      // so that we get the plain list for mobile
      if($('#js-top-navigation-menu').is(':hidden')) {
        $('#js-top-navigation-menu').removeAttr('style');
      }
    });
  });

  // ------- SEARCH ------

  // click on checkbox submits form
  $('input[type="checkbox"]').change(function(event){
    // each time a new box is checked we should reset to page 1
    // (if nothing else ther may not be a page 2 in new result)
    $('#search-form').find('[type=hidden][name=page]').val('1');
    $('#search-form').submit();
  });

  // submit keyword
  // intercept button in order to reset page param
  $('#keysearch').click(function(){
  // $('#keysearch').on('click', function() {
    console.log(" -- reached keysearch");
    $('#search-form').find('[type=hidden][name=page]').val('1')
    $('#search-form').submit();
  });

  // Hijack submission and re-route to AJAX
  // per: https://realpython.com/blog/python/django-and-ajax-form-submissions/
  $('#search-form').on('submit', function(event){
      event.preventDefault();
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
            $('#results').html(json)
            // scroll to top of results
            $('html,body').animate({
                scrollTop: $("#search-form").offset().top - 30},
                'slow');
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            //$('#results').html("<div class='alert-box alert radius' data-alert>
            //Oops! We have encountered an error: "+errmsg+
                //" <a href='#' class='close'>&times;</a></div>"); 
                // add the error to the dom
            console.log(xhr.status ); // provide a bit more info about 
            // the error to the console
            $('#results').html(errmsg + xhr.responseText); 
        }
    }); 
  };

  // link to clear search
  $('#clear').click(function(event){
    event.preventDefault();
    var searchForm = $('#search-form')
    // Clear entire form
    $('input[name="q"]').val('')
    // searchForm.find('input:text').val('');
    searchForm.find('input:checkbox')
         .removeAttr('checked').removeAttr('selected');
    // each time we clear we should reset to page 1
    $('#search-form').find('[type=hidden][name=page]').val('1')
    // submit
    searchForm.submit()
    
  });

  // more checkboxes
  // class is attached to p, though click is on "a" tag
  $('.control-box--more').click(function(){
    // toggle the short-list class
    $(this).parent().find(".control-box--list").toggleClass("short-list");
    $(this).hide();
    // console.log("----- p:nth-child(4): " + $(this).parent().parent().
      // find("p:nth-child(4)").html());
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

  // ------- MORE AND LESS TEXT ------

  // more text
  $('.body-text--more').click(function(){
    $('#more-text').toggleClass("hidden");
    $(this).hide();
    // console.log("----- p:nth-child(4): " + $(this).parent().parent().
      // find("p:nth-child(4)").html());
    $('.body-text--less').show();
    //$(this).parent().find("p:nth-child(4)").show();
  });

  // more text
  $('.body-text--less').click(function(){
    $('#more-text').toggleClass("hidden");
    $(this).hide();
    $('.body-text--more').show();
    // scroll to or near top -- once the "more" text collapses we're down at the bottom
    // of the page
    $('html,body').animate({
        scrollTop: $("#scroll-less-top").offset().top - 30},
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
