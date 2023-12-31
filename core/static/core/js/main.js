jQuery.noConflict(),
  (function ($) {
    $(window).load(function () {
      "use strict";
      $("img.retina").each(function () {
        var t = $(this),
          e = t.attr("data-fullsrc");
        t.attr("width", t.width()),
          t.attr("height", t.height()),
          window.devicePixelRatio >= 1.5 && t.attr("src", e);
      });
      var t = function () {
        if ($("body").is(".sticky-menu")) {
          var t = $(window).width(),
            e = $("header.header").outerHeight(),
            i = 3.5;
          t >= 960 && (i = 2.5),
            e > 68 &&
              $(".wrap.full-wrap").css("padding-top", e / 16 + i + "em");
        }
      };
      t();
      var e = function () {
        $(".mt-insert").each(function () {
          var t = $("img", this).height(),
            e = $(".wp-caption-text", this),
            i = $(".wp-caption-text", this).height();
          $(this).css("min-height", t),
            e.length >= 1 &&
              ($(this).css("min-height", t + i),
              $(".wp-caption", this).css("min-height", t + i),
              $(this).addClass("remove-abs"));
        });
      };
      e(),
        $(window).resize(function () {
          e(), t();
        }),
        $(".part-gallery").length > 0 &&
          $(".part-gallery .flexslider").flexslider({
            smoothHeight: !0,
            directionNav: !1,
          });
    }),
      $(document).ready(function () {
        "use strict";
        $("html").addClass("js").removeClass("no-js"),
          (navigator.userAgent.match(/iPhone/i) ||
            navigator.userAgent.match(/Android/i) ||
            navigator.userAgent.match(/Windows Phone/i) ||
            navigator.userAgent.match(/Blackberry/i)) &&
            $("body").addClass("mobile"),
          navigator.userAgent.match(/iPad/i) && $("body").addClass("ipad"),
          (navigator.userAgent.match(/iPhone/i) ||
            navigator.userAgent.match(/iPad/i)) &&
            $("body").addClass("ios"),
          ie9 && $("body").addClass("ie9");
        var t =
            /Chrome/.test(navigator.userAgent) &&
            /Google Inc/.test(navigator.vendor),
          e =
            /Safari/.test(navigator.userAgent) &&
            /Apple Computer/.test(navigator.vendor);
        if (
          ((t || e) && $("body").addClass("blur-enabled"),
          $("body").is(".home"))
        ) {
          var i = $("header.header").outerHeight();
          $(function () {
            $(".hero a.more-arrow").on("click", function () {
              if (
                location.pathname.replace(/^\//, "") ===
                  this.pathname.replace(/^\//, "") &&
                location.hostname === this.hostname
              ) {
                var t = $(this.hash);
                if (
                  ((t = t.length ? t : $("[name=" + this.hash.slice(1) + "]")),
                  t.length)
                )
                  return (
                    $("html,body").animate(
                      { scrollTop: t.offset().top - i },
                      750
                    ),
                    !1
                  );
              }
            });
          });
          var a = function () {
            var t = $(window).height();
            $(".hero").length > 0 &&
              $(".hero").css("height", t).css("position", "relative");
          };
          a(),
            $(window).resize(function () {
              a();
            });
        }
        if (
          ($("#btt").length > 0 &&
            $("#btt").on("click", function (t) {
              t.preventDefault(),
                $("html, body").animate({ scrollTop: 0 }, 800);
            }),
          $(".search-trigger").on("click", function (t) {
            t.preventDefault(),
              $("#topsearch").fadeToggle(),
              $("#topsearch input.s").focus(),
              $("body").toggleClass("overlay-active");
          }),
          $(".menu-trigger").on("click", function (t) {
            t.preventDefault(),
              $("body").toggleClass("menu-active"),
              setTimeout(function () {}, 1e3);
          }),
          $(".share-overlay").length > 0)
        ) {
          $(".share-inner").prepend(
            '<a class="share-close" href="#"><i class="fa fa-times"></i></a>'
          );
          var n = $(".share-label"),
            o = $("h1").text();
          $(".share-inner ").prepend("<h1 />"),
            $(".share-inner h1").prepend(o),
            $(".share-inner h1").prepend(n),
            $(".share-link").on("click", function (t) {
              t.preventDefault(),
                $("body").addClass("overlay-active"),
                $(".share-overlay").addClass("show").animate({ opacity: 1 });
            });
          var r = function () {
            $(".share-overlay").animate({ opacity: 0 }),
              setTimeout(function () {
                $(".share-overlay").removeClass("show"),
                  $("body")
                    .removeClass("overlay-active")
                    .removeClass("menu-active"),
                  $("#topsearch").fadeOut();
              }, 250);
          };
          $(".share-close").on("click", function (t) {
            t.preventDefault(), r();
          }),
            $(document).keyup(function (t) {
              27 === t.keyCode && r();
            });
        }
        if (
          ($(function () {
            $(".mt-tabs").each(function () {
              var t = $(".tab-inner > div", this);
              $(" ul a", this)
                .click(function (e) {
                  return (
                    e.preventDefault(),
                    t.hide().filter(this.hash).show(),
                    $(this)
                      .parent()
                      .parent()
                      .find("li")
                      .removeClass("tab-active"),
                    $(this).parent().addClass("tab-active"),
                    !1
                  );
                })
                .filter(":first")
                .click();
            });
          }),
          $(function () {
            $(".toggle").each(function () {
              var t = $(".toggle-inner", this).hide(),
                e = $(".toggle-title", this),
                i = $(this).attr("data-id");
              "open" === i &&
                ($(".toggle-inner", this).show(), e.addClass("active")),
                e.on("click", function (i) {
                  i.preventDefault(), t.slideToggle(), e.toggleClass("active");
                });
            });
          }),
          $("article").fitVids(),
          $(".gallery-item a img").each(function () {
            var t = $(this).attr("title");
            $(this).parent().attr("title", t);
          }),
          $(".wp-caption").each(function () {
            $(this).css("width", "");
          }),
          $("body").is(".page-template-t-portfolio-filter-php"))
        ) {
          var s = $(".portfolio-items");
          s.isotope({ itemSelector: ".basic-item", layoutMode: "fitRows" }),
            $(".filter-trigger").on("click", function (t) {
              t.preventDefault(), $(".filter ul").toggle();
            }),
            $(".filter ul a").on("click", function () {
              var t = $(this).attr("data-filter");
              return s.isotope({ filter: t }), !1;
            }),
            $(".filter ul li a").on("click", function (t) {
              t.preventDefault(),
                $(".filter ul li a").removeClass("active"),
                $(this).addClass("active");
            });
        }
      });








      
  })(jQuery);




