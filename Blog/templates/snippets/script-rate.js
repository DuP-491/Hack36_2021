const rating = document.querySelector('.rating')
const selects = document.querySelectorAll('[type*="radio"]')
for(i=0;i<selects.length;i++){
  selects[i].addEventListener('change', elegir)
}
function elegir(e) {
    const star = e.target
    rating.innerText=`your ratin is: ${star.value}`
  console.log(`your ratin is: ${star.value}`)
  }