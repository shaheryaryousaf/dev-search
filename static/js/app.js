// Get search form & page links
let searchForm = document.getElementById('search__form')
let pageLinks = document.getElementsByClassName('page-link')

// Ensure search form exists
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault()

      // Get data attribute
      let page = this.dataset.page

      // Add hidden search input to form
      searchForm.innerHTML += `<input value=${page} name="page" hidden />`

      // Submit Form
      searchForm.submit()
    })
  }
}
