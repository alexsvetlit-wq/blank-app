import streamlit as st

st.set_page_config(page_title="BRIS CERAMIC", layout="wide")

# Скрываем стандартный UI Streamlit, чтобы страница выглядела как самостоятельный сайт
st.markdown(
    """
    <style>
      header[data-testid="stHeader"] { display: none; }
      footer { display: none; }
      .block-container { padding-top: 0.5rem; padding-bottom: 0.5rem; max-width: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Font Awesome (иконки)
st.markdown(r"""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">""", unsafe_allow_html=True)

# CSS твоей страницы (убрали отступы в каждой строке, чтобы Streamlit НЕ превращал в code block)
st.markdown(r"""<style>
* {
box-sizing: border-box;
margin: 0;
padding: 0;
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
background: #f5f5f5;
color: #333333;
padding: 20px;
min-height: 100vh;
}

.container {
max-width: 1200px;
margin: 0 auto;
background: #ffffff;
border-radius: 12px;
padding: 30px;
box-shadow: 0 2px 15px rgba(0, 0, 0, 0.08);
border: 1px solid #eaeaea;
}

h1 {
text-align: center;
color: #2c6bbf;
margin-bottom: 20px;
font-size: 36px;
padding-bottom: 15px;
border-bottom: 2px solid rgba(44, 107, 191, 0.2);
font-weight: 700;
}

h3 {
color: #333333;
margin: 25px 0 15px;
font-size: 22px;
text-align: center;
font-weight: 600;
}

.description {
text-align: center;
color: #666666;
margin-bottom: 25px;
font-size: 16px;
line-height: 1.6;
}

/* Контактная сетка */
.contacts-grid {
display: grid;
grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
gap: 15px;
margin: 20px 0;
}

.contact-card {
padding: 20px;
background: #f8f9fa;
border: 1px solid #e0e0e0;
border-radius: 8px;
transition: all 0.3s ease;
position: relative;
}

.contact-card:hover {
background: #f0f4f8;
border-color: #2c6bbf;
transform: translateY(-2px);
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.contact-name {
font-weight: 600;
color: #222222;
margin-bottom: 12px;
font-size: 16px;
display: flex;
align-items: center;
}

.contact-name i {
margin-right: 10px;
color: #2c6bbf;
}

.contact-phone, .contact-email {
display: block;
color: #444444;
text-decoration: none;
margin: 8px 0;
font-size: 15px;
transition: color 0.3s ease;
display: flex;
align-items: center;
}

.contact-phone:hover, .contact-email:hover {
color: #2c6bbf;
}

.contact-phone i, .contact-email i {
margin-right: 10px;
width: 16px;
text-align: center;
}

/* Обновленный стиль для метки отдела продаж */
.contact-role {
position: absolute;
top: -8px;
right: -8px;
background: #2c6bbf;
color: white;
font-size: 11px;
font-weight: bold;
padding: 4px 10px;
border-radius: 20px;
}

/* Сетка для разделов */
.size-grid {
display: grid;
grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
gap: 20px;
margin: 30px 0;
}

.size-item {
padding: 20px 15px;
text-align: center;
background: linear-gradient(135deg, #2c6bbf 0%, #1a5aaf 100%);
border: 1px solid #2c6bbf;
border-radius: 12px;
transition: all 0.25s ease;
min-height: 100px;
display: flex;
align-items: center;
justify-content: center;
box-shadow: 0 4px 12px rgba(44, 107, 191, 0.2);
color: #ffffff;
}

.size-item:hover {
background: linear-gradient(135deg, #1a5aaf 0%, #0d4a9f 100%);
border-color: #1a5aaf;
transform: translateY(-3px);
box-shadow: 0 6px 18px rgba(44, 107, 191, 0.3);
}

.size-item a {
color: #ffffff;
text-decoration: none;
font-weight: 700;
font-size: 16px;
display: block;
width: 100%;
height: 100%;
display: flex;
align-items: center;
justify-content: center;
flex-direction: column;
transition: color 0.25s ease;
}

.size-item:hover a { color: #ffffff; }

.size-code {
display: block;
font-weight: 800;
color: #ffffff;
margin-bottom: 8px;
font-size: 20px;
}

.size-desc {
display: block;
color: rgba(255, 255, 255, 0.9);
font-size: 14px;
font-weight: 600;
}

.new-label {
position: absolute;
top: -8px;
right: -8px;
background: #e74c3c;
color: white;
font-size: 12px;
font-weight: bold;
padding: 4px 10px;
border-radius: 20px;
}

.item-container {
position: relative;
}

.footer {
text-align: center;
margin-top: 40px;
color: #666666;
font-size: 14px;
padding-top: 20px;
border-top: 1px solid #eaeaea;
}

.footer a {
color: #2c6bbf;
text-decoration: none;
}

.footer a:hover {
text-decoration: underline;
}

/* Стили для кнопок */
.button-row {
display: flex;
justify-content: center;
gap: 12px;
margin: 20px 0;
flex-wrap: wrap;
}

.blue-button {
display: inline-flex;
align-items: center;
padding: 12px 22px;
background: #2c6bbf;
color: white;
text-decoration: none;
border-radius: 6px;
font-weight: 600;
font-size: 14px;
transition: all 0.3s ease;
border: none;
cursor: pointer;
box-shadow: 0 2px 6px rgba(44, 107, 191, 0.2);
}

.blue-button:hover {
background: #1a5aaf;
transform: translateY(-2px);
box-shadow: 0 4px 10px rgba(44, 107, 191, 0.3);
}

.blue-button i {
margin-right: 8px;
font-size: 14px;
}

.address-info {
text-align: center;
margin-bottom: 20px;
color: #444444;
}

.address-info i {
margin-right: 8px;
color: #2c6bbf;
}

/* Адаптивность */
@media (max-width: 768px) {
.contacts-grid {
grid-template-columns: 1fr;
}

.size-grid {
grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
gap: 15px;
}

.size-item {
padding: 20px 15px;
min-height: 100px;
}

.size-code {
font-size: 20px;
}

.size-desc {
font-size: 14px;
}

.button-row {
flex-direction: column;
align-items: center;
gap: 10px;
}

.blue-button {
width: 100%;
max-width: 250px;
justify-content: center;
}
}

@media (max-width: 480px) {
.size-grid {
grid-template-columns: 1fr;
}

body {
padding: 15px;
}

.container {
padding: 20px;
}

h1 {
font-size: 28px;
}

h3 {
font-size: 20px;
}

.blue-button {
padding: 10px 18px;
font-size: 13px;
}

.contact-role {
font-size: 10px;
padding: 3px 8px;
}
}

/* Стиль для кнопки скачивания */
.download-container {
text-align: center;
margin: 30px 0;
}

.download-button {
display: inline-block;
padding: 14px 28px;
background: #2c6bbf;
color: white;
text-decoration: none;
border-radius: 6px;
font-weight: 600;
transition: all 0.3s ease;
box-shadow: 0 2px 6px rgba(44, 107, 191, 0.2);
}

.download-button:hover {
background: #1a5aaf;
transform: translateY(-2px);
box-shadow: 0 4px 10px rgba(44, 107, 191, 0.3);
}

.download-button i {
margin-right: 8px;
}

:root {
--brand: #2c6bbf;
--brand-dark: #1a5aaf;
--accent: #e74c3c;
}

h1 { color: var(--brand); border-bottom: 2px solid rgba(44, 107, 191, 0.2); }
.contact-name i, .address-info i, .blue-button:hover { color: var(--brand); }
.blue-button { background: var(--brand); }
.blue-button:hover { background: var(--brand-dark); }
.new-label { background: var(--accent); }

/* Top nav */
.topnav {
position: sticky;
top: 0; z-index: 50;
backdrop-filter: blur(8px);
background: rgba(255, 255, 255, 0.95);
border-bottom: 1px solid #eaeaea;
}
.topnav-inner { justify-content: center !important;
max-width:1200px; margin:0 auto; padding:10px 20px;
display:flex; align-items:center; gap:16px; justify-content:space-between;
}
.topnav .menu { display:flex; gap:14px; flex-wrap:wrap; }
.topnav a {
color:#333333; text-decoration:none; font-weight:600; font-size:14px;
padding:8px 10px; border-radius:6px; transition:all .2s;
}
.topnav a:hover { background:rgba(44, 107, 191, 0.1); color:var(--brand); }
.spacer { height:8px; }
/* Sections */
section { scroll-margin-top: 70px; }
.section-title{ text-align:center; font-size:26px; margin:20px 0 8px; color: #333333; }
.section-sub{ text-align:center; color:#666666; margin-bottom:16px;}
/* Map embeds */
.map-grid{
display:grid; grid-template-columns: repeat(auto-fit, minmax(280px,1fr));
gap:16px; margin: 10px 0 20px;
}
.map-embed { width:100%; height:300px; border:0; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,.1); }
/* Cards CTA row */
.cta-row{ display:flex; justify-content:center; gap:12px; flex-wrap:wrap; margin: 10px 0 20px;}
.ghost-button{ background:transparent; border:1px solid #d0d0d0; padding:12px 22px; border-radius:6px; color:#333333; text-decoration:none; font-weight:600; }
.ghost-button:hover{ border-color: #2c6bbf; color: #2c6bbf; background: rgba(44, 107, 191, 0.05); }
/* Copy button */
.copy-btn{
margin-left:auto; background:transparent; border:1px solid #d0d0d0;
color:#333333; font-size:12px; padding:4px 8px; border-radius:6px; cursor:pointer;
}
.contact-card{ display:flex; flex-direction:column; gap:6px; }
.contact-header{ display:flex; align-items:center; gap:10px; }

/* Modal for contacts */
.modal-overlay{
position: fixed; inset: 0;
background: rgba(0,0,0,.5);
display: none;
align-items: center; justify-content: center;
z-index: 1000;
backdrop-filter: blur(2px);
}
.modal-overlay.show{ display: flex; }
.modal{
width: min(900px, 92vw);
max-height: 85vh;
overflow: auto;
background: #ffffff;
border: 1px solid #e0e0e0;
border-radius: 12px;
box-shadow: 0 10px 40px rgba(0,0,0,.15);
padding: 18px 18px 8px;
color: #333333;
animation: mfade .18s ease-out;
}
.modal header{
display:flex; align-items:center; justify-content:space-between; gap:8px;
padding-bottom:8px; margin-bottom:10px;
border-bottom:1px solid #eaeaea;
}
.modal h3{ margin:0; font-size:20px; color: #333333; }
.modal .close-btn{
background: transparent; color:#333333;
border:1px solid #d0d0d0;
border-radius:8px; padding:6px 10px; cursor:pointer;
font-weight:600;
}
.modal .close-btn:hover{ border-color: #2c6bbf; color: #2c6bbf;}
@keyframes mfade { from {opacity:0; transform: translateY(6px);} to {opacity:1; transform: translateY(0);} }

/* Compact contact cards */
.contact-card {
padding: 10px 14px;
min-height: unset;
}
.contact-name {
font-size: 15px;
margin-bottom: 4px;
}
.contact-phone, .contact-email {
font-size: 14px;
margin: 3px 0;
}
.contacts-grid {
gap: 10px;
}

/* Pulsating badge animation */
@keyframes pulseGlow {
0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 87, 34, 0.5); }
70% { transform: scale(1.08); box-shadow: 0 0 10px 5px rgba(255, 87, 34, 0); }
100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 87, 34, 0); }
}
.badge {
animation: pulseGlow 2.5s infinite;
}

/* Nav primary button (same as blue-button) */
.nav-primary {
display: inline-flex;
align-items: center;
padding: 10px 16px;
background: var(--brand);
color: #fff;
text-decoration: none;
border-radius: 6px;
font-weight: 600;
font-size: 14px;
transition: all .2s ease;
border: none;
cursor: pointer;
box-shadow: 0 2px 6px rgba(44, 107, 191, 0.2);
}
.nav-primary:hover {
background: var(--brand-dark);
transform: translateY(-1px);
box-shadow: 0 4px 10px rgba(44, 107, 191, 0.3);
}
.topnav .menu .nav-primary + .nav-primary { margin-left: 10px; }

.nav-primary .icon {
margin-right: 8px;
line-height: 1;
}

.topnav .menu .blue-button {
display: inline-flex;
align-items: center;
justify-content: center;
background: var(--brand);
color: #fff !important;
border-radius: 6px;
padding: 10px 16px;
margin-left: 10px;
font-weight: 600;
text-decoration: none;
transition: background .2s ease, transform .2s ease;
}
.topnav .menu .blue-button:hover {
background: var(--brand-dark);
transform: translateY(-1px);
}

/* Transparent nav buttons */
.topnav .menu a.blue-button,
.topnav .menu a[href^="mailto:"],
.topnav .menu .nav-primary {
background: transparent;
color: #333333 !important;
border: 1px solid #d0d0d0;
border-radius: 6px;
padding: 10px 16px;
font-weight: 600;
text-decoration: none;
transition: all .25s ease;
display: inline-flex;
align-items: center;
justify-content: center;
}
.topnav .menu a.blue-button:hover,
.topnav .menu a[href^="mailto:"]:hover,
.topnav .menu .nav-primary:hover {
background: rgba(44, 107, 191, 0.1);
border-color: #2c6bbf;
transform: translateY(-1px);
}
.topnav .menu a.blue-button .icon {
margin-right: 6px;
}

/* Compact line spacing for description text */
.description {
line-height: 1.3;
margin-bottom: 10px;
}

/* --- Modal sizing optimizations --- */
.modal{
width: min(960px, 94vw);
max-height: 80vh;
overflow-x: hidden; /* убираем горизонтальный скролл */
}
#contactsModalBody{
overflow-y: auto;   /* вертикальный скролл внутри */
}
/* Контактная сетка внутри модалки уже + центрирование и запас под паддинги */
#contactsModalBody .contacts-grid{
max-width: 840px;
margin: 0 auto;
}
@media (max-width: 1024px){
.modal{ width: min(860px, 94vw); max-height: 82vh; }
#contactsModalBody .contacts-grid{ max-width: 780px; }
}
@media (max-width: 640px){
.modal{ width: 94vw; max-height: 86vh; }
#contactsModalBody .contacts-grid{ max-width: 100%; }
}

.topnav .menu .blue-button {
min-width: 180px;
text-align: center;
padding: 10px 14px;
font-size: 14px;
justify-content: center;
flex: 1 1 auto;
}
.topnav .menu {
display: flex;
flex-wrap: wrap;
justify-content: center;
gap: 10px;
}
@media (max-width: 768px) {
.topnav .menu .blue-button {
min-width: 140px;
font-size: 13px;
padding: 8px 10px;
}
}

/* === Global width & spacing optimizations === */
.topnav-inner,
.container {
max-width: 1080px !important;
margin: 0 auto;
}
.container {
padding: 24px !important;
}

/* Единая рабочая ширина для основных сеток и рядов кнопок */
.size-grid,
.contacts-grid,
section .button-row {
max-width: 1000px;
margin: 0 auto;
}

/* Сетка каталога — немного плотнее */
.size-grid {
gap: 16px !important;
}

/* Сетка контактов — два ровных ряда при десктопе */
.contacts-grid {
display: grid;
grid-template-columns: repeat(4, minmax(220px, 1fr));
gap: 16px !important;
}
@media (max-width: 1024px) {
.contacts-grid { grid-template-columns: repeat(2, minmax(240px, 1fr)); }
}
@media (max-width: 600px) {
.contacts-grid { grid-template-columns: 1fr; }
}

/* Кнопочные ряды — единая ширина и аккуратные отступы */
section .button-row {
justify-content: center !important;
gap: 10px !important;
}

/* Заголовки и абзацы — немного компактнее */
h1 { font-size: 34px !important; margin-bottom: 16px !important; }
.section-title { font-size: 24px !important; margin: 16px 0 8px !important; }
.description { line-height: 1.35 !important; margin-bottom: 12px !important; }

/* Карточки плиток — чуть компактнее */
.size-item { min-height: 92px !important; padding: 18px 14px !important; }
.size-code { font-size: 18px !important; }
.size-desc { font-size: 13.5px !important; }

/* Карточки контактов — аккуратная ширина */
.contact-card { max-width: 300px; width: 100%; margin: 0 auto; padding: 12px 14px !important; }
.contact-name { font-size: 15px !important; margin-bottom: 6px !important; }
.contact-phone, .contact-email { font-size: 14px !important; }

/* Кнопки в шапке — уже оптимизированы, добавим ещё лёгкую компоновку */
.topnav .menu { gap: 8px !important; }
.topnav .menu .blue-button { min-width: 170px !important; padding: 10px 12px !important; }
@media (max-width: 768px){
.topnav .menu .blue-button { min-width: 140px !important; }
}

/* Футер — компактнее */
.footer { margin-top: 28px !important; }

/* WhatsApp icon tint */
.contact-phone .fa-whatsapp { color: #25D366; }

/* Footer buttons styled like topnav buttons */
.footer .button-row .blue-button{
background: transparent;
color: #333333 !important;
border: 1px solid #d0d0d0;
border-radius: 6px;
padding: 10px 16px;
font-weight: 600;
text-decoration: none;
transition: all .25s ease;
display: inline-flex;
align-items: center;
justify-content: center;
min-width: 170px;
}
.footer .button-row .blue-button:hover{
background: rgba(44, 107, 191, 0.1);
border-color: #2c6bbf;
transform: translateY(-1px);
}
@media (max-width: 768px){
.footer .button-row .blue-button{ min-width: 140px; }
}

/* Нижние кнопки — стиль как в верхнем меню */
.footer .button-row .blue-button {
background: transparent;
color: #333333 !important;
border: 1px solid #d0d0d0;
border-radius: 6px;
padding: 10px 16px;
font-weight: 600;
text-decoration: none;
transition: all .25s ease;
display: inline-flex;
align-items: center;
justify-content: center;
min-width: 170px;
}
.footer .button-row .blue-button:hover {
background: rgba(44, 107, 191, 0.1);
border-color: #2c6bbf;
transform: translateY(-1px);
}
@media (max-width: 768px){
.footer .button-row .blue-button { min-width: 140px; }
}



#mailModalBackdrop {position: fixed; inset: 0; background: rgba(0,0,0,.45); display:none; align-items:center; justify-content:center; z-index: 9999;}
#mailModal {background: #fff; width: min(520px, 92vw); border-radius: 14px; box-shadow: 0 10px 30px rgba(0,0,0,.15);}
#mailModal header {padding: 16px 20px; border-bottom: 1px solid #eee; display:flex; align-items:center; justify-content:space-between;}
#mailModal h3 {margin:0; font-size: 18px; color: #333333;}
#mailModal .close {border:none; background:transparent; font-size: 22px; line-height: 1; cursor:pointer; color: #666;}
#mailModal .content {padding: 16px 20px;}
#mailProviders {display:grid; grid-template-columns: 1fr 1fr; gap: 10px;}
#mailProviders button {padding: 12px; border: 1px solid #e6e6e6; border-radius: 10px; cursor:pointer; text-align:left; font-size: 15px; background: #fafafa;}
#mailProviders button:hover {border-color: #2c6bbf; box-shadow: 0 3px 8px rgba(44, 107, 191, 0.1);}
#mailProviders .hint {display:block; font-size:12px; color:#666; margin-top:4px;}
#mailRemember {display:flex; align-items:center; gap: 8px; margin-top: 12px; font-size: 14px; color:#333;}
#mailModal footer {padding: 14px 20px; border-top: 1px solid #eee; display:flex; gap:10px; justify-content:flex-end;}
#mailModal .ghost {background:#f6f6f6; border:1px solid #e6e6e6; color: #333;}
#mailModal .primary {background:#2c6bbf; color:#fff; border:none;}
#mailModal .primary, #mailModal .ghost {padding:10px 14px; border-radius:10px; cursor:pointer;}
@media (max-width: 420px){#mailProviders{grid-template-columns:1fr;}}


#tg-float{
position:fixed;bottom:20px;right:20px;z-index:9999;
background:#2c6bbf;color:#fff;padding:12px 16px;border-radius:50px;
text-decoration:none;font-weight:600;box-shadow:0 2px 8px rgba(44, 107, 191, 0.3);
}
#tg-float:hover{background:#1a5aaf;}

#tg-float-left{
position:fixed;bottom:20px;left:20px;z-index:9999;
background:#2c6bbf;color:#fff;padding:12px 16px;border-radius:50px;
text-decoration:none;font-weight:600;box-shadow:0 2px 8px rgba(44, 107, 191, 0.3);
}
#tg-float-left:hover{background:#1a5aaf;}

/* === STREAMLIT OVERRIDE: кнопки-ссылки === */
a.blue-button,
a.blue-button:visited,
a.blue-button:hover,
a.blue-button:active {
    color: #ffffff !important;
    text-decoration: none !important;
}

a.blue-button {
    background: #2c6bbf !important;
}

a.blue-button:hover {
    background: #1a5aaf !important;
}

</style>""", unsafe_allow_html=True)

# HTML контент (убрали отступы в каждой строке, чтобы Streamlit НЕ превращал в code block)
st.markdown(r"""<!-- Остальной HTML код остается без изменений -->
<div class="topnav">
<div class="topnav-inner">
<div style="display:flex;align-items:center;gap:10px;">

</div>
<div class="menu">
<a href="https://www.brisceramic.com/" target="_blank" class="blue-button">🌐 Перейти на сайт</a>
<a id="emailLink" href="#" class="blue-button">✉️ Написать письмо</a>
</div>
</div>
</div>
<div class="spacer"></div>

<div class="container">

<h1><a href="https://www.brisceramic.com/" target="_blank" style="text-decoration: none; color: inherit;">BRIS CERAMIC</a></h1>
<p class="description">Выберите керамогранит из нашего ассортимента. Более 150+ контейнеров в наличии.</p>
<p class="description">Номер в названии фото в облаке соответствует номеру артикула в остатках.</p>

<section id="catalog">

<div class="size-grid">
<!-- Блоки каталогов -->
<div class="item-container">
<div class="size-item">
<a href="https://cloud.mail.ru/public/y9oa/582e9ReTF">
<span class="size-code">60X60</span>
<span class="size-desc">Уличная 20 мм R11</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<a href="https://cloud.mail.ru/public/YfY8/RqvgBNoVZ">
<span class="size-code">20X120</span>
<span class="size-desc">Доски</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<a href="https://cloud.mail.ru/public/jkKr/PGYV7A22X">
<span class="size-code">60X60</span>
<span class="size-desc">Матовая</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<a href="https://cloud.mail.ru/public/truv/TZD9jYukY">
<span class="size-code">60X60</span>
<span class="size-desc">Полировка</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<a href="https://cloud.mail.ru/public/VGWt/3BZcruwN4">
<span class="size-code">60X60</span>
<span class="size-desc">Карвинг</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<a href="https://cloud.mail.ru/public/KV2o/ScuuZsJQT">
<span class="size-code">60X120</span>
<span class="size-desc">Матовая</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<a href="https://cloud.mail.ru/public/rSue/gf2b2yzFQ">
<span class="size-code">60X120</span>
<span class="size-desc">Полировка</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<a href="https://cloud.mail.ru/public/F3kN/wssdawzG5">
<span class="size-code">60X120</span>
<span class="size-desc">Карвинг</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<a href="https://clck.ru/3M5ZrQ">
<span class="new-label">Остатки</span>
<span class="size-code">Ежедневные</span>
<span class="size-desc">включая "в пути" </span>
</a>
</div>
</div>

<!-- Новые добавленные элементы -->
<div class="item-container">
<div class="size-item">
<span class="new-label">Новинки</span>
<a href="https://cloud.mail.ru/public/Dxh4/hcYPWdQeg">
<span class="size-code">60X60/120х60</span>
<span class="size-desc">(все поверхности)</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<span class="new-label">Распродажи</span>
<a href="https://cloud.mail.ru/public/wZiT/Gpe44mJHL">
<span class="size-code">60X60/120х60/20х120</span>
<span class="size-desc">(обновляются)</span>
</a>
</div>
</div>
<div class="item-container">
<div class="size-item">
<span class="new-label">Прайс</span>
<a href="https://cloud.mail.ru/public/bQ3B/vgEgE7yzg">
<span class="size-code">ОПТ+SALE</span>
<span class="size-desc">(актуальный)</span>
</a>
</div>
</div>
</div>
</section>

<section id="stocks">


</div>
</div>
</div>
</section>

<!-- Обновленный блок контактов -->
<section id="contacts">
<h2 class="section-title">Свяжитесь с нами:</h2>

<div class="contacts-grid">
<div class="contact-card">
<div class="contact-name"><i class="fas fa-envelope"></i> Эл.почта для заказов</div>
<a href="mailto:info@brisceramic.com" class="contact-email">info@brisceramic.com</a>
</div>

<div class="contact-card">

<div class="contact-name"><i class="fas fa-user"></i> Анна Хворова</div>
<a href="https://wa.me/79034205888" target="_blank" rel="noopener" class="contact-phone" aria-label="Открыть WhatsApp чат с номером"><i class="fab fa-whatsapp"></i> +7-903-420-5-888</a>
</div>

<div class="contact-card">

<div class="contact-name"><i class="fas fa-user"></i> Анна Поротикова</div>
<a href="https://wa.me/79601241544" target="_blank" rel="noopener" class="contact-phone" aria-label="Открыть WhatsApp чат с номером"><i class="fab fa-whatsapp"></i> +7-960-124-15-44</a>
</div>

<div class="contact-card">

<div class="contact-name"><i class="fas fa-user"></i> Андрей Шишкин</div>
<a href="https://wa.me/79030257999" target="_blank" rel="noopener" class="contact-phone" aria-label="Открыть WhatsApp чат с номером"><i class="fab fa-whatsapp"></i> +7-903-025-7-999</a>
</div>

<div class="contact-card">

<div class="contact-name"><i class="fas fa-user"></i> Сергей Таратухин</div>
<a href="https://wa.me/79601079415" target="_blank" rel="noopener" class="contact-phone" aria-label="Открыть WhatsApp чат с номером"><i class="fab fa-whatsapp"></i> +7-960-107-94-15</a>
</div>

<div class="contact-card">

<div class="contact-name"><i class="fas fa-user"></i> Елена Лукьянченко</div>
<a href="https://wa.me/79065842407" target="_blank" rel="noopener" class="contact-phone" aria-label="Открыть WhatsApp чат с номером"><i class="fab fa-whatsapp"></i> +7-906-584-24-07</a>
</div>

<div class="contact-card">

<div class="contact-name"><i class="fas fa-warehouse"></i> Складская поддержка</div>
<a href="mailto:kostuhov81@rambler.ru" class="contact-email"><i class="fas fa-envelope"></i> kostuhov81@rambler.ru</a>
</div>

<div class="contact-card">
<div class="contact-name"><i class="fas fa-user-tie"></i> Начальник склада</div>
<a href="https://wa.me/79288490581" target="_blank" rel="noopener" class="contact-phone" aria-label="Открыть WhatsApp чат с номером"><i class="fab fa-whatsapp"></i> +7-928-849-05-81</a>
</div>
</div>

<!-- Обновленный блок с кнопками -->
<div style="text-align: center; margin: 20px 0;">


<div class="button-row">
<a href="https://yandex.ru/maps/-/CLfJAC~e" class="blue-button"><i class="fas fa-map-marked-alt"></i> Склад Крымск, ул. Привокзальная 68а</a>
<a href="https://yandex.ru/maps/-/CLAcfC5H" class="blue-button"><i class="fas fa-map-marked-alt"></i> Склад Воронеж, ул. Холмистая 1е, склад №5</a>
</div>

</div>
</section>
<div class="button-row">
<a href="https://cloud.mail.ru/public/e7BX/UjvmnpmQM" target="_blank" class="blue-button">📚 Перейти в каталоги</a>

<a href="https://cloud.mail.ru/public/JPzy/sXZBJaX5v" target="_blank" class="blue-button">📁 Файлы для скачивания</a>
<a href="https://cloud.mail.ru/public/tYhv/iSYgAEbbQ" class="blue-button">🧩 Мерчендайзинг</a>
</div>
<div class="button-row" style="margin-top:6px;">
<a class="ghost-button" href="#top">Наверх</a>
</div>


<div class="footer">
<p>главный офис : Москва, Деребеневская наб.11 (БЦ Полларс)</p>
<p>директор: <a href="tel:+7-980-240-77-77">+7-980-240-77-77</a></p>
</div>
</div>

<!-- Contacts Modal -->
<div class="modal-overlay" id="contactsModal" role="dialog" aria-modal="true" aria-labelledby="contactsTitle">
<div class="modal">
<header>
<h3 id="contactsTitle">Контакты отдела продаж</h3>
<button class="close-btn" id="contactsClose" aria-label="Закрыть">Закрыть</button>
</header>
<div id="contactsModalBody">
<!-- contacts content injected here -->
</div>
</div>
</div>

<div id="mailModalBackdrop" role="dialog" aria-modal="true" aria-labelledby="mailModalTitle">
<div id="mailModal">
<header>
<h3 id="mailModalTitle">Выбор почтового сервиса</h3>
<button class="close" aria-label="Закрыть" id="mailCloseBtn">×</button>
</header>
<div class="content">
<div id="mailProviders">
<button data-url="https://mail.yandex.ru/compose?to=info%40brisceramic.com&subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="yandex"><strong>Яндекс.Почта</strong><span class="hint">mail.yandex.ru</span></button>
<button data-url="https://mail.google.com/mail/?view=cm&fs=1&to=info%40brisceramic.com&su=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="gmail"><strong>Gmail</strong><span class="hint">mail.google.com</span></button>
<button data-url="https://outlook.live.com/mail/0/deeplink/compose?to=info%40brisceramic.com&subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="outlook"><strong>Outlook</strong><span class="hint">outlook.live.com</span></button>
<button data-url="https://e.mail.ru/compose/?to=info%40brisceramic.com&subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="mailru"><strong>Mail.ru</strong><span class="hint">mail.ru</span></button>
<button data-url="https://compose.mail.yahoo.com/?to=info%40brisceramic.com&subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="yahoo"><strong>Yahoo Mail</strong><span class="hint">mail.yahoo.com</span></button>
<button data-url="mailto:info@brisceramic.com?subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="mailto"><strong>Системный почтовик</strong><span class="hint">mailto:</span></button>
</div>
<label id="mailRemember"><input type="checkbox" id="mailRememberChk"> Запомнить выбор</label>
</div>
<footer>
<button class="ghost" id="mailCancelBtn">Отмена</button>
<button class="primary" id="mailOpenLastBtn">Открыть последний выбранный</button>
</footer>
</div>
</div>

<script>
(function(){
var link = document.getElementById('emailLink');
if (!link) return;

var ua = navigator.userAgent || '';
var defaultKey = /YaBrowser/i.test(ua) ? 'yandex' : 'gmail';

// Ensure link href is a valid mailto for long-press / copy-link
link.setAttribute('href', link.getAttribute('href') || 'mailto:info@brisceramic.com?subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A');

// Inject modal into DOM
var backdrop = document.createElement('div');
backdrop.innerHTML = `<div id="mailModalBackdrop" role="dialog" aria-modal="true" aria-labelledby="mailModalTitle">  <div id="mailModal">    <header>      <h3 id="mailModalTitle">Выбор почтового сервиса</h3>      <button class="close" aria-label="Закрыть" id="mailCloseBtn">×</button>    </header>    <div class="content">      <div id="mailProviders">        <button data-url="https://mail.yandex.ru/compose?to=info%40brisceramic.com&subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="yandex"><strong>Яндекс.Почта</strong><span class="hint">mail.yandex.ru</span></button>        <button data-url="https://mail.google.com/mail/?view=cm&fs=1&to=info%40brisceramic.com&su=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="gmail"><strong>Gmail</strong><span class="hint">mail.google.com</span></button>        <button data-url="https://outlook.live.com/mail/0/deeplink/compose?to=info%40brisceramic.com&subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="outlook"><strong>Outlook</strong><span class="hint">outlook.live.com</span></button>        <button data-url="https://e.mail.ru/compose/?to=info%40brisceramic.com&subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="mailru"><strong>Mail.ru</strong><span class="hint">mail.ru</span></button>        <button data-url="https://compose.mail.yahoo.com/?to=info%40brisceramic.com&subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="yahoo"><strong>Yahoo Mail</strong><span class="hint">mail.yahoo.com</span></button>        <button data-url="mailto:info@brisceramic.com?subject=%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%9F%D1%80%D0%BE%D1%88%D1%83%20%D0%B2%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%80%D1%82%D0%B8%D0%BA%D1%83%D0%BB%D1%8B%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0%20%3A" data-key="mailto"><strong>Системный почтовик</strong><span class="hint">mailto:</span></button>      </div>      <label id="mailRemember"><input type="checkbox" id="mailRememberChk"> Запомнить выбор</label>    </div>    <footer>      <button class="ghost" id="mailCancelBtn">Отмена</button>      <button class="primary" id="mailOpenLastBtn">Открыть последний выбранный</button>    </footer>  </div></div>`;
document.body.appendChild(backdrop.firstElementChild);
var modalBackdrop = document.getElementById('mailModalBackdrop');

function openModal(){
modalBackdrop.style.display = 'flex';
document.body.style.overflow = 'hidden';
// focus first button
var firstBtn = document.querySelector('#mailProviders button');
if (firstBtn) firstBtn.focus();
}
function closeModal(){
modalBackdrop.style.display = 'none';
document.body.style.overflow = '';
}
function openInNewTab(url){
try { window.open(url, '_blank', 'noopener'); return true; } catch(e){ return false; }
}

function getStore(){
try {
var raw = localStorage.getItem('mailPicker');
return raw ? JSON.parse(raw) : {};
} catch(e){ return {}; }
}
function setStore(obj){
try { localStorage.setItem('mailPicker', JSON.stringify(obj)); } catch(e){}
}

var store = getStore();
var lastKey = store.lastKey || defaultKey;
document.getElementById('mailOpenLastBtn').addEventListener('click', function(){
var btn = document.querySelector('#mailProviders button[data-key="'+lastKey+'"]') ||
document.querySelector('#mailProviders button[data-key="'+defaultKey+'"]');
if (btn) {
var url = btn.getAttribute('data-url');
openInNewTab(url);
closeModal();
}
});

// Events
link.addEventListener('click', function(e){
e.preventDefault();
openModal();
});

document.getElementById('mailCancelBtn').addEventListener('click', closeModal);
document.getElementById('mailCloseBtn').addEventListener('click', closeModal);
modalBackdrop.addEventListener('click', function(e){
if (e.target === modalBackdrop) closeModal();
});
document.addEventListener('keydown', function(e){
if (e.key === 'Escape') closeModal();
});

// Provider buttons
Array.prototype.forEach.call(document.querySelectorAll('#mailProviders button'), function(btn){
btn.addEventListener('click', function(){
var url = btn.getAttribute('data-url');
var key = btn.getAttribute('data-key');
var remember = document.getElementById('mailRememberChk').checked;
openInNewTab(url);
if (remember) setStore({lastKey:key, ts: Date.now()});
closeModal();
});
});
})();
</script>


<style>
#tg-float{
position:fixed;bottom:20px;right:20px;z-index:9999;
background:#2c6bbf;color:#fff;padding:12px 16px;border-radius:50px;
text-decoration:none;font-weight:600;box-shadow:0 2px 8px rgba(44, 107, 191, 0.3);
}
#tg-float:hover{background:#1a5aaf;}

#tg-float-left{
position:fixed;bottom:20px;left:20px;z-index:9999;
background:#2c6bbf;color:#fff;padding:12px 16px;border-radius:50px;
text-decoration:none;font-weight:600;box-shadow:0 2px 8px rgba(44, 107, 191, 0.3);
}
#tg-float-left:hover{background:#1a5aaf;}
</style>
<a id="tg-float" href="https://t.me/Brisceramic" target="_blank">📢 Telegram</a>
<a id="tg-float-left" href="https://drive.google.com/drive/u/1/folders/1IsRAngkIbCbHgbUt_PzG7jppDsne-QoL">📚 Библиотека</a>""", unsafe_allow_html=True)
