const btnAdd = document.getElementsByName("send")
const btnGet = document.getElementsByName("get")
const api = "http://127.0.0.1:8000/api/notes/"


async function sendNote(event) {
    event.preventDefault()

    const form = event.target;
    const formSendResult = document.querySelector('.add-result')
    formSendResult.textContent = '';

    // const formData = new FormData(form)
    // const formDataObject = Object.fromEntries(formData.entries())

    // console.log(formDataObject)

    const {author, text} = Object.fromEntries(new FormData(form).entries())

    try {
        btnAdd.textContent = 'Loading...';
        const res = await fetch(api, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'author': author,
                'text': text
            })
        });

        if (res.ok) {
            const data = await res.json()

            formSendResult.textContent = `ID: ${data.num}`;
            form.reset();
        } else {
            throw new Error(res.statusText)
        }
    } catch (error) {
        console.error(error);
        formSendResult.textContent = 'BAD';
    } finally {
        btnAdd.textContent = 'Send'
    }

}


async function getNote(event) {
    event.preventDefault()

    const form = event.target
    const formSendResult = document.querySelector('.get-result')
    formSendResult.textContent = '';

    const noteAuthor = document.querySelector('.note__author')
    const noteTime = document.querySelector('.note__time')
    const noteText = document.querySelector('.note__text')
    const info = document.querySelector('.messages')

    const id = Object.fromEntries(new FormData(form).entries()).idp
    console.log(id)

    try {
        console.log(api + id)
        const res = await fetch(api + 'num/' + id)

        if(res.ok) {
            const data = await res.json()
            console.log(data)

            if (data.detail){
                info.textContent = data.detail
            } else{
                noteAuthor.textContent = `Author: ${data.author}`
                noteTime.textContent = `Time: ${data.time}`
                noteText.textContent = `${data.text}`
            }
        }  else {
            throw new Error(res.statusText)
        }

    } catch (error) {
        console.error(error);
    }
}