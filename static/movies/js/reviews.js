const $addReviewBtn = document.querySelector('.add-review-btn')
const $closeReviewModal = document.querySelector('.close-modal')
const $modal = document.querySelector('.add-review-modal')
const $textArea = document.querySelector('#review-field')
const $form = document.forms.review
const $radioButtons = document.querySelectorAll('.rating-start')

const isTargetContainsClass = (target, name) => {
    return target.classList.contains(name)
}

$addReviewBtn.addEventListener('click', () => {
    $modal.classList.remove('hide')
})

$closeReviewModal.addEventListener('click', (e) => {
    $modal.classList.add('hide')
})

$modal.addEventListener('click', (e) => {
    const target = e.target
    if (isTargetContainsClass(target, 'add-review-modal')) {
        $modal.classList.add('hide')
    }
})

let reviewValue = ''
$textArea.addEventListener('change', (e) => {
    reviewValue = e.target.value
})

$form.addEventListener('submit', (e) => {
    e.preventDefault()

    let currentRating = null
    $radioButtons.forEach(el => {
        if (el.checked) {
            currentRating = el.value
        }
    })

    if(!currentRating) return

    try {
        const currentUrl = window.location.href;
        const crf_token = document.getElementsByName('csrfmiddlewaretoken')[0].getAttribute('value');
        const response =  fetch(`${currentUrl}review-create/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': crf_token
            },
            body: JSON.stringify({
                'rating': currentRating,
                'text': reviewValue,
                'user_id': userData
            }),
        });
            setTimeout(() => {
                window.location.reload()

    }, 1000);

    } catch (error) {
        alert(error);
    }




})

