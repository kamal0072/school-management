How to use Google maps in django application >
Make a django project by running command>django-admin startproject project_name
cd project name


make a application by running command >python manage.py startapp app_name
make any templates 




and then make accound on mapbox and copy some lines 

<div id='map' style='width: 400px; height: 300px;'></div>




<script>
mapboxgl.accessToken = 'pk.eyJ1Ijoia2FtYWwwMDcyIiwiYSI6ImNrcDNsMmlhcDI0c3gyd21wZ2x2aThkbTAifQ.4wFDwS-374kWTE0_j37mVA';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11'
});
</script>



These lines of code you have to add in the head tag
now fire up the server python manage.py runserver
