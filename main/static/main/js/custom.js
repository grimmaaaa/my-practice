	
 $(document).ready(function(){
		$('.slider-div').owlCarousel({
		loop: true,
		margin:0,
		autoplay:true,
		slideSpeed: 300,
		nav:false,
		dots:true,
		animateIn: 'fadeIn',
		
		responsive: {
			0: {
				items:1
			},
			600: {
				items:1
			},
			667: {
			items:1
			},
			768: {
				items:1
			},
			1000: {
				items:1,
			}
			
		}
		
	})
  
});


$(document).ready(function(){
	$('.slider-testi').owlCarousel({
	loop: true,
	margin:30,
	autoplay:true,
	nav:false,
	dots:true,
	responsive: {
		0: {
			items:1
		},
		600: {
			items:1
		},
		667: {
		items:1
		},
		1000: {
			items:1
		}
	}
})

});


$(document).ready(function(){
	$('.slou-products').owlCarousel({
	loop: true,
	margin:30,
	autoplay:true,
	nav:false,
	dots:true,
	responsive: {
		0: {
			items:1
		},
		600: {
			items:1
		},
		667: {
		items:2
		},
		1000: {
			items:4
		}
	}
})

});


$(document).ready(function(){
	$('.slider-packges').owlCarousel({
	loop: true,
	margin:30,
	autoplay:true,
	nav:false,
	dots:true,
	responsive: {
		0: {
			items:1
		},
		600: {
			items:1
		},
		667: {
		items:2
		},
		1000: {
			items:4
		}
	}
})

});


$(document).ready(function(){
	$('.tems-slider-02').owlCarousel({
	loop: true,
	margin:30,
	autoplay:true,
	nav:false,
	dots:true,
	responsive: {
		0: {
			items:1
		},
		600: {
			items:1
		},
		667: {
		items:1
		},
		1000: {
			items:2
		}
	}
})





});



$(document).ready(function(){
	$('.logos-ldert').owlCarousel({
	loop: true,
	margin:30,
	autoplay:true,
	nav:false,
	dots:true,
	responsive: {
		0: {
			items:1
		},
		600: {
			items:1
		},
		667: {
		items:2
		},
		768: {
			items:3
		},
		1000: {
			items:6
		}
	}
})





});


$(document).ready(function(){
	$("#customRadio1").click(function(){
	  $("#ac-2").hide();
	});
	$("#customRadio1").click(function(){
	  $("#ac-1").show();
	});
	 $("#customRadio2").click(function(){
	  $("#ac-1").hide();
	});
	$("#customRadio2").click(function(){
	  $("#ac-2").show();
	});
});

$(document).ready(function () {


    $('.shop-slider').owlCarousel({
    loop: true,
    margin:30,
    autoplay:true,
    nav:false,
    dots:true,
    responsive: {
        0: {
            items:1
        },
        600: {
            items:1
        },
        667: {
          items:2
        },
        1000: {
            items:4
        }
    }
 })
  });

$(function() {
	$( "#datepicker" ).datepicker();
  });
  
// counting js

var a = 0;
$(window).scroll(function() {

  var oTop = $('#counter').offset().top - window.innerHeight;
  if (a == 0 && $(window).scrollTop() > oTop) {
    $('.counter-value').each(function() {
      var $this = $(this),
        countTo = $this.attr('data-count');
      $({
        countNum: $this.text()
      }).animate({
          countNum: countTo
        },

        {

          duration: 2000,
          easing: 'swing',
          step: function() {
            $this.text(Math.floor(this.countNum));
          },
          complete: function() {
            $this.text(this.countNum);
            //alert('finished');
          }

        });
    });
    a = 1;
  }

});

$(document).ready(function() {
    $( window ).scroll(function() {
          var height = $(window).scrollTop();
          if(height >= 100) {
              $('header').addClass('fixed-menu');
          } else {
              $('header').removeClass('fixed-menu');
          }
      });
  });

  $(document).ready(function () {
	var selector = '.sixe-menu-q li';
	
	  $(selector).on('click', function(){
		  $(selector).removeClass('active');
		  $(this).addClass('active');
	  });
});


(function () {
    "use strict";
    var jQueryPlugin = (window.jQueryPlugin = function (ident, func) {
      return function (arg) {
        if (this.length > 1) {
          this.each(function () {
            var $this = $(this);
  
            if (!$this.data(ident)) {
              $this.data(ident, func($this, arg));
            }
          });
  
          return this;
        } else if (this.length == 1) {
          if (!this.data(ident)) {
            this.data(ident, func(this, arg));
          }
  
          return this.data(ident);
        }
      };
    });
  })();
  
  (function () {
    "use strict";
    function Guantity($root) {
      const element = $root;
      const quantity = $root.first("data-quantity");
      const quantity_target = $root.find("[data-quantity-target]");
      const quantity_minus = $root.find("[data-quantity-minus]");
      const quantity_plus = $root.find("[data-quantity-plus]");
      var quantity_ = quantity_target.val();
      $(quantity_minus).click(function () {
        quantity_target.val(--quantity_);
      });
      $(quantity_plus).click(function () {
        quantity_target.val(++quantity_);
      });
    }
    $.fn.Guantity = jQueryPlugin("Guantity", Guantity);
    $("[data-quantity]").Guantity();
  })();




  $('.sponsors-categories').on( 'click', 'a', function() {
	var $this = $(this);
	// get group key
	var $buttonGroup = $this.parents('.button-group');
	var filterGroup = $buttonGroup.attr('data-filter-group');
	// set filter for group
	filters[ filterGroup ] = $this.attr('data-filter');
	// combine filters
	var filterValue = concatValues( filters );
	// set filter for Isotope
	$container.isotope({ filter: filterValue });
  });















    // expro hall

	$(document).ready(function(){
                
		$(".expo").slice(0,12).show();
		$("#viewall").click(function(e){
			e.preventDefault();
			$(".expo:hidden").slice(0,84).fadeIn("slow");
			
			if($(".expo:hidden").length == 0){
			$("#viewall").fadeOut("slow");
			}
		});
	
	
		$(".expo-Exhibitors").click(function(e){
			e.preventDefault();
		   
			if($(".term-exhibitors").length < 12){
				$("#viewall").hide();
			 }

	
				$(".term-exhibitors").hide();
				 $(".term-exhibitors").slice(0,12).show();
	
				 $("#viewall").click(function(e){
					e.preventDefault();
					$(".term-exhibitors:hidden").slice(0,84).fadeIn("slow");
					
					if($(".term-exhibitors:hidden").length == 0){
					$("#viewall").fadeOut("slow");
					}
				});
		});
	
		$(".expo-Startup").click(function(e){
			e.preventDefault();
			if($(".term-startup-showcase").length < 12){
				$("#viewall").hide();
			} 
	
			 $(".term-startup-showcase").hide();
				 $(".term-startup-showcase").slice(0,12).show();
	
				 $("#viewall").click(function(e){
					e.preventDefault();
					$(".term-startup-showcase:hidden").slice(0,84).fadeIn("slow");
					
					if($(".term-startup-showcase:hidden").length == 0){
					$("#viewall").fadeOut("slow");
					}
				});
	
		});
	
	});