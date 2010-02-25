jQuery.fn.adjustPanel = function() {
    jQuery(this).find("ul, .subpanel").removeAttr("style"); //Reset sub-panel and ul height

    var windowHeight = jQuery(window).height(); //Get the height of the browser viewport
    var panelsub = jQuery(this).find(".subpanel").height(); //Get the height of sub-panel
    var panelAdjust = windowHeight - 100; //Viewport height - 100px (Sets max height of sub-panel)
    var ulAdjust =  panelAdjust - 25; //Calculate ul size after adjusting sub-panel

    if ( panelsub > panelAdjust ) {	 //If sub-panel is taller than max height...
        jQuery(this).find(".subpanel").css({ 'height' : panelAdjust }); //Adjust sub-panel to max height
        jQuery(this).find("ul").css({ 'height' : panelAdjust}); ////Adjust subpanel ul to new size
    }
    else { 
        //If sub-panel is smaller than max height...
        jQuery(this).find("ul").removeAttr("style"); 
    }
};

/* XXX: References to alertpanel needs to be refactored out... */
jQuery("#alertpanel").adjustPanel(); //Run the adjustPanel function on #alertpanel

//Each time the viewport is adjusted/resized, execute the function
jQuery(window).resize(function () {
    jQuery("#alertpanel").adjustPanel();
});

jQuery(document).ready(function() {

    //Click event outside of subpanel
    jQuery(document).click(function() { 
        //Click anywhere and...
        jQuery(".subpanel").hide(); //hide subpanel
        jQuery("#footpanel li a").removeClass('active'); //remove active class on subpanel trigger
    });
    jQuery('.subpanel ul').click(function(e) {
        e.stopPropagation(); //Prevents the subpanel ul from closing on click
    });

    //Show/Hide delete icons on Alert Panel
    jQuery("#alertpanel li").hover(function() {
        jQuery(this).find("a.delete").css({'visibility': 'visible'}); //Show delete icon on hover
    },function() {
        jQuery(this).find("a.delete").css({'visibility': 'hidden'}); //Hide delete icon on hover out
    });
});
