from django.urls import path
from . import views


urlpatterns=[
    path('masterpage',views.linking_masterpage,name='masterpage'),
    path('',views.linking_home,name='home'),
    path('about',views.linking_about,name='about'),
    path('contact',views.linking_contact,name='contact'),
    path('new',views.linking_new,name='new'),
    path('try',views.linking_try,name='try'),
    path('baabtra',views.linking_baabtra,name='baabtra'),
    path('baabtra2',views.linking_baabtra2,name='baabtra2'),
    path('about1',views.linking_about1,name='about1'),
    path('blog',views.linking_blog,name='blog'),
    path('login',views.linking_login,name='login'),
    path('newpage',views.linking_newpage,name='newpage'),
    path('browser',views.linking_browser,name='browser'),
    path('cssrule',views.linking_cssrule,name='cssrule'),
    path('grid',views.linking_grid,name='grid'),
    path('gridaline',views.linking_gridaline,name='gridaline'),
    path('grid1',views.linking_grid1,name='grid1'),
    path('machinetest',views.linking_machinetest,name='machinetest'),
    path('facebook',views.linking_facebook,name='facebook'),
    path('forgot',views.linking_forgot,name='forgot'),
    path('fpro',views.linking_fpro,name='fpro'),
    path('fmess',views.linking_fmess,name='fmess'),
    path('js',views.linking_js,name='js'),
    path('js1',views.linking_js1,name='js1'),
    path('fact',views.linking_fact,name='fact'),
    path('pali',views.linking_pali,name='pali'),
    path('funcion',views.linking_funcion,name='funcion'),
    path('sumpr',views.linking_sumpr,name='sumpr'),
    path('eveod',views.linking_eveod,name='eveod'),
    path('sumdi',views.linking_sumdi,name='sumdi'),
    path('fun1',views.linking_fun1,name='fun1'),
    path('countele',views.linking_countele,name='countele'),
    path('large',views.linking_large,name='large'),
    path('fib',views.linking_fib,name='fib'),
    path('dom',views.linking_dom,name='dom'),
    path('largesec',views.linking_largesec,name='largesec'),
    path('dom2',views.linking_dom2,name='dom2'),
    path('dom3',views.linking_dom3,name='dom3'),
    path('pattern',views.linking_pattern,name='pattern'),
    path('array',views.linking_array,name='array'),
    path('todo',views.linking_todo,name='todo'),
    path('dom4',views.linking_dom4,name='dom4'),
    path('dom5',views.linking_dom5,name='dom5'),
    path('jq',views.linking_jq,name='jq'),
    path('jq1',views.linking_jq1,name='jq1'),
    path('jq2',views.linking_jq2,name='jq2'),
    path('jqvalidation',views.linking_jqvalidation,name='jqvalidation'),
    path('mttodo',views.linking_mttodo,name='mttodo'),
     path('newtodo',views.linking_newtodo,name='newtodo'),
     path('calc',views.linking_calc,name='calc'),




    



    
    

]
