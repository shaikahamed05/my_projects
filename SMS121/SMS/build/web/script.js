const wrapper=document.querySelector('.wrapper');
const wrapper1=document.querySelector('.wrapper1');
const wrapper2=document.querySelector('.wrapper2');
const btnstudentPopup=document.querySelector('.btnstudentLogin-popup');
const btnstaffPopup=document.querySelector('.btnstaffLogin-popup');
const btnadminPopup=document.querySelector('.btnadminLogin-popup');
const iconClose=document.querySelector('.icon-close');
const iconClose1=document.querySelector('.icon-close1');
const iconClose2=document.querySelector('.icon-close2');



btnstudentPopup.addEventListener('click',()=> {
	wrapper.classList.add('active-popup');
	
});

btnstaffPopup.addEventListener('click',()=> {
	wrapper1.classList.add('active-popup');
	
});

btnadminPopup.addEventListener('click',()=> {
	wrapper2.classList.add('active-popup');
	
});

iconClose.addEventListener('click',()=> {
	wrapper.classList.remove('active-popup');
	
});

iconClose1.addEventListener('click',()=> {
	wrapper1.classList.remove('active-popup');
	
});

iconClose2.addEventListener('click',()=> {
	wrapper2.classList.remove('active-popup');
	
});

