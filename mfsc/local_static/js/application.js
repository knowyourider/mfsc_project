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

  // assign click to checkboxes
  $('input[type="checkbox"]').change(function(event){
    // alert('radio button clicked value: ' + $(event.target).attr('value'));
    $('form[name="menu"]').submit()   
  });

  // ------- SEARCH ------
  // link to clear search
  $('#clear').click(function(event){
    // clear the value in the search field
    $('input[name="q"]').val('')
    // submit
    $('form[name="menu"]').submit()
    
  });

  // toggle search box for checkboxes
  // class is attached to p, though click is on a tag
  $('.control-box--toggle').click(function(){
    //console.log("----- got to more ");
    // must be a better way to find what is actuall previous sibling
    // toggle the short-list class
    // $(this).parent().find(".control-box--list").toggleClass("short-list");
    // $(this).parent().parent().find(".control-box--list").toggleClass("short-list");
    $(this).parent().find(".control-box--list").toggleClass("short-list");
    //$(this).parent().hide();
    $(this).hide();
    // console.log("----- p:nth-child(4): " + $(this).parent().parent().find("p:nth-child(4)").html());
    // $(this).parent().parent().find("p:nth-child(4)").show();
    $(this).parent().find("p:nth-child(4)").show();
  });

  // toggle search box for checkboxes
  $('.control-box--fewer').click(function(){
    // $(this).parent().parent().find(".control-box--list").toggleClass("short-list");
    $(this).parent().find(".control-box--list").toggleClass("short-list");
    $(this).hide();
    // $(this).parent().parent().find("p:nth-child(3)").show();
    $(this).parent().find("p:nth-child(3)").show();
    // try scrolling
    // scrollTop: $("#divToBeScrolledTo").offset().top
    $('html,body').animate({
        // scrollTop: $("#"+id).offset().top},
        scrollTop: $("#by-tag").offset().top - 50},
        'slow');
    // scrollTop( 300 );
  });

  // ------- MENU PAGINATION ------

  // Turn page selection into form submit
  // aug and q parameters are in the form and will be submited 
  $('#paging > ul > li.page-nav').click(function(event){
    event.preventDefault();
    // get the page number from href
    var chosen_href = $(event.target).closest('li').children('a').attr('href');
    var href_split = chosen_href.split('=');  
    // page number = href_split[1]  
    // alert('in page nav. page num: ' + href_split[1]); 
    // set the page number in the hidden field
    $('form[name="menu"]').find('[type=hidden][name=page]').val(href_split[1])
    $('form[name="menu"]').submit()
  });


});	// end doc ready
