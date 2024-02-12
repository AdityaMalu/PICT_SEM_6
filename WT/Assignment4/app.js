/**
 * @param {Event} e 
 */
function handleSubmit(e){
    const {firstName,lastName, m,s,cs} = e.target
    const avg = (parseInt(m.value)+parseInt(s.value) + parseInt(cs.value))/3
    alert(`Hello ${firstName.value} ${lastName.value} your average score is ${avg}`)
    e.preventDefault();
}

const form = document.getElementById('form')
form.addEventListener('submit',handleSubmit)