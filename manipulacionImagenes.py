<!DOCTYPE HTML>
<html lang="es">
<head>
    <link rel="icon" href="/resources/theme-zen/images/favicon.png" rel="icon"></link>
    <!--[if IE]><link rel="shortcut icon" href="/resources/theme-zen/images/favicon.ico" type="image/x-icon" /><![endif]-->
    <title>Funciones y librerias necesarias</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="keywords" content="accessibility, portals, elearning, design">
    <meta name="robots" content="all">
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="generator" lang="en" content="OpenACS version 5.5.1">
    <link rel="stylesheet" href="/resources/dotlrn/dotlrn-toolbar.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/acs-templating/forms.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/acs-templating/lists.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/tds-lib/lib/swiper/dist/css/swiper.min.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/theme-zen/css/bootstrap.min.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/tds-lib/lib/animate.css/animate.min.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/tds-lib/css/tds-lib.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/acs-subsite/default-master.css" type="text/css" media="screen">
    <link rel="stylesheet" href="/resources/tds-lib/css/tds-fonts.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/theme-zen/css/main.css" type="text/css" media="screen">
    <link rel="stylesheet" href="/resources/tda-notifications/notificationspanel/resources/css/notifications.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/theme-zen/css/print.css" type="text/css" media="print">
    <link rel="stylesheet" href="/resources/theme-zen/css/handheld.css" type="text/css" media="handheld">
    <link rel="stylesheet" href="/resources/tda-notifications/css/style.css" type="text/css" media="all">
    <link rel="stylesheet" href="/resources/theme-zen/css/color/green.css" type="text/css" media="screen">
    <link rel="alternate stylesheet" href="/resources/theme-zen/css/highContrast.css" title="highContrast" type="text/css" media="all">
    <link rel="alternate stylesheet" href="/resources/tda-notifications/css/style.highContrast.css" title="highContrast" type="text/css" media="all">
    <link rel="alternate stylesheet" href="/resources/tda-notifications/notificationspanel/resources/css/notifications.highContrast.css" title="highContrast" type="text/css" media="all">
    <link rel="alternate stylesheet" href="/resources/theme-zen/css/508.css" title="508" type="text/css" media="all">
    <link rel="alternate stylesheet" href="/resources/tds-lib/css/tds-lib.highContrast.css" title="highContrast" type="text/css" media="all">
   <script type="text/javascript" src="/resources/acs-subsite/core.js"></script>

   <script type="text/javascript" src="/resources/theme-zen/js/reloj.js"></script>

   <script type="text/javascript" src="/resources/tds-lib/js/tds-lib.js"></script>

   <script type="text/javascript" src="/resources/theme-zen/js/styleswitcher.js"></script>

   <script type="text/javascript" src="/resources/tds-lib/js/tds-lib.utilities.js"></script>


</head>
<body onload="antesclock();">






    







  
<meta name="viewport" content="width=device-width, initial-scale=1">
<div id="notifications-grid" class="no-text-selectable notifications-grid arrow_box" aria-hidden="true">
	<header>
		<h2 class="tds-lib_title_04">Notificaciones</h2>
		<div class="options">
			<button class="delete-all-notifications-button" aria-label="Eliminar Notificaciones">
				<i class="tds-lib-icon-delete"></i>
			</button>
		</div>
	</header>
	<section class="notifications-container">
		<!-- Swiper -->
		<div class="notifications-categories" id="notifications-categories" role="tablist" tabindex="0" aria-label="Lista de navegación de notificaciones. Presione tab para moverse a la primera categoría de notificaciones. Puede presionar las teclas izquierda y derecha para moverse a través de las notificaciones.">
			<!-- Categories loaded using handlebars -->
		</div>
		<div class="swiper-container notifications-panel" id="notifications-panel">
			<!-- Categories Notifications loaded using handlebars lib-->
			<div class="loading">
				<i class="tds-lib-icon-load tds-lib-spin"></i>
			</div>
		</div>
	</section>
	<div class="delete_all_overlay" tabindex="-1">
		<section class="delete_all_popup" id="delete_all_popup" aria-hidden="true" role="dialog" aria-labelledby="delete_all_popup_heading" aria-describedby="delete_all_popup_description">
			<h2 id="delete_all_popup_heading" class="tds-lib_title_04">Eliminar Notificaciones</h2>
			<p id="delete_all_popup_description">¿Se eliminarán todas las notificaciones, está seguro?</p>
			<div class="options">
				<button class="tds-lib_form primary delete_all_notifications_button confirm">Aceptar</button>
				<button class="tds-lib_form delete_all_notifications_button cancel">Cancelar</button>
			</div>
		</section>
	</div>
</div>
<!-- We add the scripts at the end of the adp for performance issues. -->
<script src="/resources/tds-lib/lib/swiper/dist/js/swiper.min.js"></script>
<script src="/resources/tds-lib/lib/handlebars/handlebars.min.js"></script>
<script src="/resources/tds-lib/lib/moment/min/moment.min.js"></script>
<script src="/resources/tds-lib/js/tds-lib.utilities.js"></script>
<script src="/resources/tda-notifications/notificationspanel/resources/js/modernizr.promise.js"></script>
<script src="/resources/tda-notifications/notificationspanel/resources/js/notifications.js"></script><form id="tiempo" name="tiempo" method="post" 
                    action="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/file-storage/view/tareas-programadas/tarea-programada-1/manipulacionImagenes.py" class="margin-form"><div><input type="hidden" name="form:mode" value="edit" ></div>
<div><input type="hidden" name="form:id" value="tiempo" ></div>
<div><input type="hidden" name="__confirmed_p" value="0" ></div><div><input type="hidden" name="__refreshing_p" value="0" ></div><div><input type="hidden" name="__submit_button_name" value="" ></div><div><input type="hidden" name="__submit_button_value" value="" ></div><div><input type="hidden" name="ehora" value="21" id="hora" ></div><div><input type="hidden" name="eminutos" value="33" id="minutos" ></div><div><input type="hidden" name="esegundos" value="27" id="segundos" ></div></form>
<div id="wrapper">
  <header id="header-td">
    <section>
      <div id="td_menu_responsive_toggle" onclick="openLeftMenu()">
        <i class="tds-lib-icon-menu3"></i>
      </div>
      <section id="logo">
        
          <a href="/dotlrn" role="link">
            <div role="image" aria-label="Logo TEC Digital" id="logoTD"></div>
          </a>
        
      </section>
      <section id="main-menu-td">
        
          <nav><li class="main_menu_td_active"><a href="/dotlrn/" tabindex='0' title="Ir a Inicio" accesskey="1">Inicio</a><li><a href="/dotlrn/courses" tabindex='0' title="Ir a Cursos"  accesskey="5">Cursos</a><li><a href="/dotlrn/communities" tabindex='0' title="Ir a Comunidades"  accesskey="6">Comunidades</a><li><a href="/dotlrn/control-panel" tabindex='0' title="Ir a Mi Cuenta"  accesskey="7">Mi Cuenta</a> </nav>
         
      </section>
      <section id="header-navigation">
      
        <ul>
          <li id="platform_user_notifications" tabindex="0" accesskey="n">
            <i role="img" aria-label="Icono Notificaciones" title="Abrir / Cerrar panel de notificaciones" class="tds-lib-icon-notification"></i>
            <div class="notifications-unread-available"></div>
          </li>
          <!-- HELP TOOLS -->
          <li id="help_tools" tabindex="0" onclick="toggle_help_panel()" accesskey="h">
            <i role="img" aria-label="Icono Ayuda" title="Abrir / Cerrar panel de ayuda" class="tds-lib-icon-help2"></i>
            <div id="platform_help_panel" class="platform_panel arrow_box">
              <div>
                <h2>Ayuda</h2>
                <a tabindex="0" href="https://tecdigital.zendesk.com/hc/es" class="text_url_01">Soporte en línea</a>
                <a tabindex="0" href="https://tecdigital.tec.ac.cr/capsulas" class="text_url_01">Ayuda</a>
                <!--<a tabindex="0" href="/tda-virtualtours" class="text_url_01">MESSAGE KEY MISSING: 'tda-virtualtours.help_panel_label'</a>-->
            </div>
          </li>
          <!--VV - Panel for log-out and profile configurations -->
          <li id="platform_user_profile" tabindex="0" onclick="toggle_profile_panel()" accesskey="p">
            <img alt='Foto de perfil de su usuario' class='platform_avatar' src="/shared/portrait-bits.tcl?user_id=29348994&size=thumbnail" >
            <div id="platform_user_panel" class="platform_panel arrow_box">
              <div id="platform_user_avatar"><img alt='Foto de perfil de su usuario' class='platform_avatar' src="/shared/portrait-bits.tcl?user_id=29348994&size=thumbnail" ></div>
              <div id="platform_user_info"><strong>ERICK ANDRES  OBREGON FONSECA </strong><br>2016123157</div>
              <div id="platform_user_logout">
                <a class="pull-right" href="/dotlrn/control-panel">Mi cuenta</a>
                <a class="pull-right" href="/theme-zen/accessibility" title="Página sobre Accesibilidad" accesskey="0">Página sobre Accesibilidad</a>
                <!--<a class="pull-right" href="/tda-um">Modelo de usuario</a>-->
              </div>
              <a accesskey="q" href="/register/logout" title="Salir de tec-digital" class="tds-lib_form tds-lib_button">Salir</a>
            </div>
          </li>
        </ul>
      
      </section>
      <section id="server-time"></section>
    </section>
  </header>
  <!-- /header -->
  <section id="content-wrapper">
    
      <section id="sub-navigation">
        <ul id='selectable_subnavbar'><li><a href="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/?page_num=0" title="Ir a TALLER DE PROGRAMACION GR 4" accesskey="H">TALLER DE PROGRAMACION GR 4</a> </li><li><a href="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/?page_num=1" title="Ir a Calendario" accesskey="C">Calendario</a> </li><li class="sub-navigation-active"><a href="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/?page_num=2" title="Ir a Documentos" accesskey="F">Documentos</a></li><li><a href="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/?page_num=3" title="Ir a Evaluaciones" accesskey="">Evaluaciones</a> </li></ul>
      </section>
    
    <section id="breadtime">
      <section id="breadcrumbs">
        <!--<span class="screen-reader-only">Está en:</span>-->
        <ul class="compact">
          
            <li id="breadcrumbs_toggle" tabindex="0">
              <i class="tds-lib-icon-breadcrumb_icon"></i>
              <ul class="arrow_box_left">
                
                  <li>
                    
                      <a href="/dotlrn">Inicio</a>
                      <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                    
                  </li>
                
                  <li>
                    
                      <a href="/dotlrn/classes/">Asignaturas</a>
                      <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                    
                  </li>
                
                  <li>
                    
                      <a href="/dotlrn/classes/E/">ESCUELA DE INGENIERIA EN ELECTRONICA</a>
                      <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                    
                  </li>
                
                  <li>
                    
                      <a href="/dotlrn/classes/E/CE1102/">TALLER DE PROGRAMACION</a>
                      <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                    
                  </li>
                
                  <li>
                    
                      <a href="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/">TALLER DE PROGRAMACION GR 4</a>
                      <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                    
                  </li>
                
                  <li>
                    
                      <a href="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/file-storage/">Documentos</a>
                      <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                    
                  </li>
                
                  <li>
                    
                      Funciones y librerias necesarias
                    
                  </li>
                
              </ul>
            </li>
            <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
            <div>
            
              <li>
                
                  <a href="/dotlrn">Inicio</a>
                  <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                
              </li>
            
              <li>
                
                  <a href="/dotlrn/classes/">Asignaturas</a>
                  <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                
              </li>
            
              <li>
                
                  <a href="/dotlrn/classes/E/">ESCUELA DE INGENIERIA EN ELECTRONICA</a>
                  <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                
              </li>
            
              <li>
                
                  <a href="/dotlrn/classes/E/CE1102/">TALLER DE PROGRAMACION</a>
                  <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                
              </li>
            
              <li>
                
                  <a href="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/">TALLER DE PROGRAMACION GR 4</a>
                  <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                
              </li>
            
              <li>
                
                  <a href="/dotlrn/classes/E/CE1102/S-1-2016.CA.CE1102.4/file-storage/">Documentos</a>
                  <i class="separator tds-lib-icon-expand_right tds-lib-16x"></i>
                
              </li>
            
              <li>
                
                  Funciones y librerias necesarias
                
              </li>
            
            </div>
          
        </ul>
      </section>
    </section>
    <div class="block-marker">Inicio del Contenido Principal</div>
    <div id="inner-wrapper">
      
        <div id="main">
          <div id="main-content" accesskey="2" tabindex="0">
            <div class="main-content-padding">
      
# -*- coding: utf-8 -*-<br>
"""<br>
Created on Sun Feb 28 09:22:13 2016<p>@author: Saul Python 2.7<br>
"""<br>
#importa una parte de la libreria, llamada misc<br>
from scipy import misc;<br>
#le pone un alias a la sub-libreria pyplot<br>
import matplotlib.pyplot as plotter</p><p>import numpy;<br>
import sys;</p><p>def test1():<br>
    #cambia el limite de la pila<br>
    sys.setrecursionlimit(10**6);<br>
    numFilas = 60;<br>
    numColumnas = 60;<br>
    #inicializacion en ceros de la imagen<br>
    imagenFiltrada = numpy.zeros((numFilas, numColumnas));<br>
    print("Test 1 running");<br>
    #lectura de la imagen en escala de grises<br>
    imagenGS = misc.imread('manNoisy.png', 1);<br>
    #muestra de la imagen en escala de grises<br>
    plotter.imshow(imagenGS, plotter.get_cmap('gray'));<br>
    plotter.show();<br>
    #ejemplo del llamado para el filtrado de la imagen<br>
    #anchoVentana = 3;<br>
    #imagenFiltrada = filtradorImagenes.filtrarPorMedianas(imagenGS, anchoVentana);<br><br>
    misc.imsave("filtrada.jpg", imagenFiltrada);<br>
    misc.imsave("original.jpg", imagenGS);<br>
    print("Terminado!");<br>
    plotter.imshow(imagenFiltrada, plotter.get_cmap('gray'));<br>
    plotter.show();<br><br><br>
test1();</p>


<script type="text/javascript" src="/resources/acs-templating/tinymce/jscripts/tiny_mce/plugins/asciimath/js/ASCIIMathMLwFallback.js"></script>
<script type="text/javascript">
    var AScgiloc = 'http://www.imathas.com/imathas/filter/graph/svgimg.php';
    var AMTcgiloc = "http://www.imathas.com/cgi-bin/mimetex.cgi";
</script>

            </div> <!-- /main-content-padding -->
          </div> <!-- /main-content -->
        </div> <!-- /main -->
      

    </div> <!-- /inner-wrapper -->
  </section> <!-- /content-wrapper -->

  <div id="footer">
    <div class="block-marker">Inicio del Pie de Página</div>

    <div id="footer-links">
      <div style="float:left;">
        <ul class="compact">
          <li><a href="http://tecdigital.tec.ac.cr/condiciones/" target="_blank">Términos y Condiciones</a></li>
        </ul>
      </div>
      <div style="float:right;">
        <ul class="compact">
          <li>Un sitio <a href="http://dotlrn.org" title="The .LRN Project Homepage">.LRN</a></li>
          <li>Powered by <a href="http://openacs.org" title="The OpenACS Project Homepage">OpenACS</a></li>
        </ul>
      </div>
      <!-- <ul class="compact">
        <li>Un sitio <a href="http://dotlrn.org" title="The .LRN Project Homepage">.LRN</a></li>
        <li>Powered by <a href="http://openacs.org" title="The OpenACS Project Homepage">OpenACS</a></li>
      </ul>-->
    </div> <!-- /footer-links -->
  </div> <!-- /footer -->
</div> <!-- /wrapper -->

<!-- VV- Menu left: Visible para disposivos pequeños -->
  <div id="menu-left" class="vpanel" data-role="left_panel">
    <!-- VV -
      El siguiente div cumple la funcionalidad de medir 75% del screen hasta 300px maximo 
      Para ver CSS vaya a: */theme-zen/www/resources/css/main.css
    -->
    <div id="menu-left-content">
      <div>
        <header>
          <img alt='Foto de perfil de su usuario' class='platform_avatar' src="/shared/portrait-bits.tcl?user_id=29348994&size=thumbnail" >
          <div>
            <h1>ERICK ANDRES  OBREGON FONSECA </h1>
            <h2>2016123157</h2>
          </div>
        </header>
        <nav><li class="main_menu_td_active"><a href="/dotlrn/" tabindex='0' title="Ir a Inicio" accesskey="1">Inicio</a><li><a href="/dotlrn/courses" tabindex='0' title="Ir a Cursos"  accesskey="5">Cursos</a><li><a href="/dotlrn/communities" tabindex='0' title="Ir a Comunidades"  accesskey="6">Comunidades</a><li><a href="/dotlrn/control-panel" tabindex='0' title="Ir a Mi Cuenta"  accesskey="7">Mi Cuenta</a> <li><a href='http://www.tec-digital.itcr.ac.cr/capsulas/' target='_blank'>Ayuda</a><li><a href='/theme-zen/accessibility' title='Página sobre Accesibilidad' accesskey='0'>Accesibilidad</a><li><a href='/register/logout' title='Salir de tec-digital'>Salir</a></nav>
      </div>
    </div>
  </div>

<script type="text/javascript" src="/resources/theme-zen/js/vpanel.js"></script>
<script>
  /* VICTOR VARGAS - SWIPE FUNCTIONALITIES FOR MOBILE MENU */
  // Initialize the left menu panel
  vpanel.init("menu-left");
  function openLeftMenu() {
    vpanel.togglePanel();
  }
  // END LEFT MENU
  /* PROFILE LOGOUT PANEL */
  var panel = document.getElementById("platform_user_panel");
  var panel_trigger = document.getElementById("platform_user_profile");
  panel.style.display = "none";
  // Toggle the user panel
  function toggle_profile_panel(){
    var p = document.getElementById("platform_user_panel");
    if (p.style.display == "none") {
      p.style.display = "block";
    } else {
      p.style.display = "none";
    }
  }
  // HELP PANEL
  var panel_help = document.getElementById("platform_help_panel");
  var panel_help_trigger = document.getElementById("help_tools");
  panel_help.style.display = "none";
  // TOGGLE HELP PANEL
  function toggle_help_panel() {
    var p = document.getElementById("platform_help_panel");
    if (p.style.display == "none") {
      p.style.display = "block";
    } else {
      p.style.display = "none";
    }
  }
  document.addEventListener("click",function(){
    panel.style.display = "none";
    panel_help.style.display = "none";
  });
  panel.addEventListener("click",function(e){
    e.stopPropagation();
  });
  panel_trigger.addEventListener("click",function(e){
    e.stopPropagation();
    document.getElementById("gn_panel").style.display = "none";
    document.getElementById("platform_help_panel").style.display = "none";
  });
  panel_help.addEventListener("click",function(e){
    e.stopPropagation();
  });
  panel_help_trigger.addEventListener("click",function(e){
    e.stopPropagation();
    document.getElementById("gn_panel").style.display = "none";
    document.getElementById("platform_user_panel").style.display = "none";
  });
  // notifications system
  var notifications_system = new notificationsSystem({
    notificationsToggleSelector: '#platform_user_notifications'
    // onDelete: function(notification) {
    //   do stuff
    // },
    // onInit: function(notification) {
    //   console.log('initialized!!!');
    // }
  });
  // ACCESIBILIDAD
  panel_help_trigger.onkeydown = function(event) {
    if ( event.which == 13 ) {
      toggle_help_panel();
    }
  }
  panel_trigger.onkeydown = function(event) {
    if ( event.which == 13 ) {
      toggle_profile_panel();
    }
  }
  var breadcrumbs_html_obj = document.querySelector("#breadcrumbs_toggle");
  var breadcrumbs_li_html_obj = breadcrumbs_html_obj.querySelectorAll("ul li");
  if ( breadcrumbs_li_html_obj.length == 1 ) {
    breadcrumbs_html_obj.querySelector("ul").style.display = "none";
    breadcrumbs_html_obj.querySelector("i").className += " disabled";
  }
  // VIRTUAL TOURS
  //virtual_tour.init('home');
</script>

  



<!-- modificado por fcontreras al 29.6.2012, para mostrar el nombre del server-->
<div style="font-size:12px;color:#D8D8D8;clear:both;margin-left: 25px;">Servidor: vLRN-07<br>Usuarios: 4 de 8</div>

</body>
</html>
