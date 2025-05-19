document.addEventListener('DOMContentLoaded', function () {
    const items = document.querySelectorAll('.event-item');
    const fixedPreview = document.getElementById('fixed-preview');
    const previewImg = fixedPreview.querySelector('img');

    if (items.length > 0) {
        const firstItem = items[0];
        const imgSrc = firstItem.dataset.img;
        
        previewImg.src = imgSrc;
        fixedPreview.classList.remove('d-none');
    }

    items.forEach(item => {
        item.addEventListener('mouseenter', () => {
            const imgSrc = item.dataset.img;
            previewImg.src = imgSrc;

            document.querySelectorAll('.event-item').forEach(el => el.classList.remove('active-item'));
            item.classList.add('active-item');
        });
    });
});