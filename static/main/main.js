$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })


  const myModal = new mdb.Modal(document.getElementById('myModal'), options)