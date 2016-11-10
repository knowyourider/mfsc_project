$(document).ready(function() {

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
