document.querySelector('button#lembretes').addEventListener('click', () => {
    document.querySelector('section#checklist').style.display = 'none';
    document.querySelector('section#lembretes').style.display = 'block';
})
document.querySelector('button#checklist').addEventListener('click', () => {
    document.querySelector('section#lembretes').style.display = 'none';
    document.querySelector('section#checklist').style.display = 'block';
})