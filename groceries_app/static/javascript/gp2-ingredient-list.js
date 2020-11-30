function deleteThisRow(row) {
    var row_index = row.parentNode.parentNode.rowIndex;
    document.getElementById("ingredients-table").deleteRow(row_index);
}

function addRow() {
    var table = document.getElementById("ingredients-table");
    var row = table.insertRow(-1);
    var deleteButton = row.insertCell(-1);
    var ingredient = row.insertCell(-1);
    var quantity = row.insertCell(-1);

    deleteButton.innerHTML = 'Delete';
    ingredient.innerHTML = 'ingredient';
    quantity.innerHTML = 'quantity';
}