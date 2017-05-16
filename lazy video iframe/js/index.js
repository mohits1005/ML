$(document).scroll(function(){
	ytVideoAutoplay();
});
function ytVideoAutoplay()
{
	// Get media - with autoplay disabled (audio or video)
	var media = $('.youtube');
	var tolerancePixel = 0;
    // Get current browser top and bottom
    var scrollTop = $(window).scrollTop() + tolerancePixel;
    var scrollBottom = $(window).scrollTop() + $(window).height() - tolerancePixel;

    media.each(function(index, el) {

        var yTopMedia = $(this).offset().top;
        var yBottomMedia = $(this).height() + yTopMedia;

        if(scrollTop < yBottomMedia && scrollBottom > yTopMedia )
        {
			if($(this).attr("already_played") != '1')
	        {
	        	console.log('yes');
	        	var iframe = document.createElement( "iframe" );
	        	$(this).attr("already_played",'1');
				iframe.setAttribute( "frameborder", "0" );
				iframe.setAttribute( "allowfullscreen", "" );
				iframe.setAttribute( "src", "https://www.youtube.com/embed/"+ this.dataset.embed +"?enablejsapi=1&rel=0&showinfo=0&autoplay=1" );
				this.innerHTML = "";
				this.appendChild( iframe );  
			}	         
        } else {
			//console.log($(el).find('iframe')[0]);
			if($(el).find('iframe').length>0)
				$(el).find('iframe')[0].contentWindow.postMessage('{"event":"command","func":"' + 'stopVideo' + '","args":""}', '*');
        }
        if($(el).find('iframe').length>0)
        {	
        	$(el).find('iframe')[0].contentWindow.postMessage('{"method":"setVolume", "value":0}','*');
    	}
    });
}