function deleteCat(catId) {
  fetch("/delete-cat", {
    method: "POST",
    body: JSON.stringify({ catId: catId }),
  }).then((_res) => {
    window.location.href = "/categorias";
  });
}