var map;
window.onload = function() {
document.getElementById("defaultOpen").click();
map = L.map("map", {
  center: [-25.45, -49.25],
  zoom: 14,

});

//2 - Camadas base

var osmColorido = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

// map.on('click', function(e) {var lat= e.latlng.lat ;
// var long = e.latlng.lng;
// alert (e)
//
//
// });

var editableLayers = new L.FeatureGroup();
map.addLayer(editableLayers);

// define custom marker
var MyCustomMarker = L.Icon.extend({
  options: {
    shadowUrl: null,
    iconAnchor: new L.Point(12, 12),
    iconSize: new L.Point(24, 24),
    iconUrl: 'http://www.pdclipart.org/albums/Buildings/igloo.png'
  }
});

var drawPluginOptions = {
  position: 'topright',
  draw: {
    polyline: {
      shapeOptions: {
        color: '#f357a1',
        weight: 10
      }
    },
    polygon: {
      allowIntersection: false, // Restricts shapes to simple polygons
      drawError: {
        color: '#e1e100', // Color the shape will turn when intersects
        message: '<strong>Oh snap!<strong> you can\'t draw that!' // Message that will show when intersect
      },
      shapeOptions: {
        color: '#bada55'
      }
    },
    circle: false, // Turns off this drawing tool
    rectangle: {
      shapeOptions: {
        clickable: false
      }
    },
    marker: {
      icon: new MyCustomMarker()
    }
  },
  edit: {
    featureGroup: editableLayers, //REQUIRED!!
    remove: false
  }
};





// Initialise the draw control and pass it the FeatureGroup of editable layers
var drawControl = new L.Control.Draw(drawPluginOptions);
map.addControl(drawControl);


var editableLayers = new L.FeatureGroup();
map.addLayer(editableLayers);




map.on('draw:created', function(e) {
  var type = e.layerType,
    layer = e.layer;

    //console.log(e.layer.toGeoJSON());
    document.getElementById('ponto').value = JSON.stringify( e.layer.toGeoJSON());

  if (type === 'marker') {
    layer.bindPopup('A popup!');
  }

  editableLayers.addLayer(layer);
});

// Get the element with id="defaultOpen" and click on it

// $('#defaultOpen').click();

}


function openCity(evt, pageName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
         //tabcontent[i].style.display = "none";
       $(tabcontent[i]).hide();
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    //document.getElementById(pageName).style.display = "blocks";
           $("#"+ pageName).show();
           map.invalidateSize();

    evt.currentTarget.className += " active";
    document.getElementById("#defaultOpen").click();
}
