this.map = L.map("map", {
  center: [40.873376751657915, -101.0536740855401], // USA coordinates
  zoom: 5,
  zoomControl: true,
  trackResize: true,
});

const tiles = L.tileLayer(
  "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
  {
    attribution: "Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ",
    maxZoom: 16,
  }
);

tiles.addTo(this.map);

fetch(`http://localhost:8000/json/kmeans/${k}/${cluster_id}`)
  .then((res) => { res.json().then(data => {
        let x = JSON.parse(data)
        console.log(x)
        L.geoJson(x, {
            pointToLayer: (feature, latlng) => {
                let redIcon = L.icon({
                    iconSize: [10, 10],
                    iconAnchor: [13, 27],
                    popupAnchor: [1, -24],
                    iconUrl: "https://img.icons8.com/material-outlined/24/000000/filled-circle--v1.png",
                });
        return L.marker(latlng, { icon: redIcon });
      },})
      .bindPopup(function (layer) {
          let output = `<strong>State</strong>: ${layer.feature.properties.state_name}<br /><strong>Coordinates</strong>: ${layer.feature.geometry.coordinates}`;
          return output;
      })
      .openPopup()
      .addTo(map)
      })
})



