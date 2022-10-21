(() => {
    const post_content = document.querySelectorAll('.post-content-p');

    for (const link of authorsLogoutLinks) {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            post_content.class = post_content
        });
    }
})();