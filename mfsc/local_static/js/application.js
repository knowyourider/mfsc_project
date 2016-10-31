$(document).ready(function() {

  $('.expander-trigger').click(function(){
    // console.log("got to trigger");
    // this works when in the a tag, and the hidden div immediately follows the a tag
    // $(this).toggleClass("expander-hidden");
    // this works when the a tag is inside of another element, in this case the li
    $(this).toggleClass("expander-hidden");
  });

});	// end doc ready
