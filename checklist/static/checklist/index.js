document.querySelector('a#register').addEventListener('click', () => {
    document.querySelector('form#login').style.display = 'none';
    document.querySelector('form#register').style.display = 'block';
});

document.querySelector('a#login').addEventListener('click', () => {
    document.querySelector('form#register').style.display = 'none';
    document.querySelector('form#login').style.display = 'block'; 
});