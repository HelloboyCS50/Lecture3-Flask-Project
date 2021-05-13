


//Shoes 


$(window).scroll(function() {
		let position = $(this).scrollTop();
		if (position >= 450) {
			$('.card-1').addClass('moveFromLeft');
			$('.card-2').addClass('moveFromRight');
			$('.card-3').addClass('moveFromBottom');
		}
		else{
			$('.card-1').removeClass('moveFromLeft');
			$('.card-2').removeClass('moveFromRight');
			$('.card-3').removeClass('moveFromBottom');
		}
});

// BagPack

$(window).scroll(function() {
		let position = $(this).scrollTop();
		if (position >= 1150) {
			$('.card-4').addClass('moveFromLeft');
			$('.card-5').addClass('moveFromRight');
			$('.card-6').addClass('moveFromBottom');
		}
		else{
			$('.card-4').removeClass('moveFromLeft');
			$('.card-5').removeClass('moveFromRight');
			$('.card-6').removeClass('moveFromBottom');
		}
});