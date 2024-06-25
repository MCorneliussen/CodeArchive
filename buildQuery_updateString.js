function buildQuery() {
      const search = document.getElementById('search-input').value
      const ordering = document.getElementById('select-ordering').value
      const order = document.getElementById('select-how-to-order').value
      const page = document.getElementById('page-number').value
      const size = document.getElementById('page-size').value

      let QueryString = ""
      let firstFilterAdded = false

      if (ordering != 'No ordering') {
        QueryString = updateString(QueryString, firstFilterAdded)
        QueryString += "sort=" + ordering + ":" + order
        firstFilterAdded = true
      }

      if (search != '') {
        QueryString = updateString(QueryString, firstFilterAdded)
        QueryString += "description=" + search
        firstFilterAdded = true
      }

      if (page != '') {
        QueryString = updateString(QueryString, firstFilterAdded)
        QueryString += "page=" + page
        firstFilterAdded = true
      }

      if (size != '') {
        QueryString = updateString(QueryString, firstFilterAdded)
        QueryString += "size=" + size
        firstFilterAdded = true
      }

      window.location.href = "/tutorials" + QueryString;


    }

    function updateString(QueryString, FirstAdded) {
      if (FirstAdded) {
        QueryString += "&"

      } else {
        QueryString += "?"
      }
      return QueryString

    }
