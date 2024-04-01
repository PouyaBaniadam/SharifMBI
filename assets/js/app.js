var listOfFuture = [
    'use strict',
    'fade',
    'fadeOut',
    'delay',
    '#preloader',
    'ready',
    'fadeIn',
    'stop',
    '.dropdown-menu',
    'find',
    'hover',
    'ul.nav li.dropdown',
    'scroll',
    'scrollTop',
    'affix',
    'removeClass',
    'nav.sticky-header',
    'addClass',
    'on',
    '.testimonialSwiper',
    '.swiper-pagination',
    '.swiper-button-next',
    '.swiper-button-prev',
    '.appTwoReviewSwiper',
    'initialize',
    'general',
    'parallax',
    '.parallax-element',
    'documentOnReady',
    'init',
    'tooltip',
    '[data-bs-toggle="tooltip"]',
    'ease-in-out',
    'iframe',
    'mfp-fade',
    'magnificPopup',
    '.popup-youtube, .popup-vimeo, .popup-gmaps',
    'inline',
    '#name',
    '.popup-with-form',
  ]
  var THEMETAGS = THEMETAGS || {}
  ;(function () {
    listOfFuture[0]
    $(window)[listOfFuture[5]](function () {
      $(listOfFuture[4])[listOfFuture[3]](100)[listOfFuture[2]](listOfFuture[1])
    })
    $(listOfFuture[11])[listOfFuture[10]](
      function () {
        $(this)
          [listOfFuture[9]](listOfFuture[8])
          [listOfFuture[7]](true, true)
          [listOfFuture[3]](100)
          [listOfFuture[6]](200)
      },
      function () {
        $(this)
          [listOfFuture[9]](listOfFuture[8])
          [listOfFuture[7]](true, true)
          [listOfFuture[3]](100)
          [listOfFuture[2]](200)
      }
    )
    $(window)[listOfFuture[18]](listOfFuture[12], function () {
      var _0x1d50x2 = $(window)[listOfFuture[13]]()
      if (_0x1d50x2 < 2) {
        $(listOfFuture[16])[listOfFuture[15]](listOfFuture[14])
      } else {
        $(listOfFuture[16])[listOfFuture[17]](listOfFuture[14])
      }
    })
    var swpr = new Swiper(listOfFuture[19], {
      slidesPerView: 2,
      speed: 700,
      spaceBetween: 30,
      slidesPerGroup: 2,
      loop: true,
      pagination: {
        el: listOfFuture[20],
        clickable: true,
      },
      breakpoints: {
        320: { slidesPerView: 1 },
        640: { slidesPerView: 1 },
        768: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        1024: {
          slidesPerView: 2,
          spaceBetween: 25,
        },
        1142: {
          slidesPerView: 2,
          spaceBetween: 30,
        },
      },
      navigation: {
        nextEl: listOfFuture[21],
        prevEl: listOfFuture[22],
      },
    })
    var swpr = new Swiper(listOfFuture[23], {
      slidesPerView: 2,
      speed: 700,
      spaceBetween: 30,
      slidesPerGroup: 2,
      loop: true,
      navigation: {
        nextEl: listOfFuture[21],
        prevEl: listOfFuture[22],
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 30,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 30,
        },
        991: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
      },
    })
    THEMETAGS[listOfFuture[24]] = {
      init: function () {
        THEMETAGS[listOfFuture[24]][listOfFuture[25]]()
      },
      general: function () {
        var _0x1d50x4 = $(listOfFuture[27])[listOfFuture[26]]({
          scalarX: 100,
          scalarY: 100,
        })
      },
    }
    THEMETAGS[listOfFuture[28]] = {
      init: function () {
        THEMETAGS[listOfFuture[24]][listOfFuture[29]]()
      },
    }
    $(document)[listOfFuture[5]](THEMETAGS[listOfFuture[28]][listOfFuture[29]])
    $(function () {
      $(listOfFuture[31])[listOfFuture[30]]()
    })
    AOS[listOfFuture[29]]({
      easing: listOfFuture[32],
      once: true,
      duration: 500,
    })
    $(listOfFuture[36])[listOfFuture[35]]({
      disableOn: 700,
      type: listOfFuture[33],
      mainClass: listOfFuture[34],
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false,
    })
    $(listOfFuture[39])[listOfFuture[35]]({
      type: listOfFuture[37],
      preloader: false,
      focus: listOfFuture[38],
    })
  })()
let dropArea = document.getElementById("drop-area");

["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
  dropArea.addEventListener(eventName, preventDefaults, false);
  document.body.addEventListener(eventName, preventDefaults, false);
});

["dragenter", "dragover"].forEach((eventName) => {
  dropArea.addEventListener(eventName, highlight, false);
});

["dragleave", "drop"].forEach((eventName) => {
  dropArea.addEventListener(eventName, unhighlight, false);
});

dropArea.addEventListener("drop", handleDrop, false);

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight(e) {
  dropArea.classList.add("highlight");
}

function unhighlight(e) {
  dropArea.classList.remove("highlight");
}

function handleDrop(e) {
  let dt = e.dataTransfer;
  let files = dt.files;
  handleFiles(files);
}

function handleFiles(files) {
  [...files].forEach(uploadFile);
}

function uploadFile(file) {
  console.log("Uploading", file.name);
}

dropArea.addEventListener("click", () => {
  fileElem.click();
});

let fileElem = document.getElementById("fileElem");
fileElem.addEventListener("change", function (e) {
  handleFiles(this.files);
});