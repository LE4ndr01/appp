document.addEventListener("keyup",(e)=>{
    locationLogin(e)
    locationIndex(e)
    // pagina que no se blanquee
    location.href(e) = locationIndex(e);


})
//Pagina inicial a Login 
const locationLogin=(e)=>{
    if(e.ctrlKey && e.key==="1"){
        console.log("Abriendo Ventana Login")
        window.location.assign("{% url 'login'%}")
        return
    }
}
//Pagina Login a Inicial
const locationIndex=(e)=>{
    if(e.ctrlKey && e.key==="q"){
        console.log("Volviendo al Inicio")
        window.location.assign("/templates/core/index.html")
        return
    }
}
//ResponsiveNav
const btn_nabvar=document.getElementById('btn_nabvar')
const navbar=document.getElementById('nabvar')
const icon=document.getElementById('icon')

btn_nabvar.addEventListener('click',()=>{
    navbar.classList.toggle('change_height')
    icon.classList.contains('fa-bars') ? icon.classList.replace('fa-bars','fa-times') : icon.classList.replace('fa-times','fa-bars')
})