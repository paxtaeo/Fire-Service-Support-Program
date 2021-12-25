function calculateTotalPrice() {
    let menu1_price = menu_list[document.getElementById('id_menu1').value] || 0;
    let menu2_price = menu_list[document.getElementById('id_menu2').value] || 0;
    let menu3_price = menu_list[document.getElementById('id_menu3').value] || 0;

    document.getElementById('total_price').innerHTML = (menu1_price + menu2_price + menu3_price).toLocaleString('ko-KR', { style: 'currency', currency: 'KRW' });
}

function setNthMenu(valueToSelect, index) {  
    index += 1;
    document.getElementById('id_menu' + index).value = valueToSelect;
}

function setMenusAsFavorites(favorites) {
    let menus = favorites.toString().split(' | ').slice(1)
    menus.forEach(setNthMenu);
}

function setDefaultValueOfDateInput() {
    var today = new Date();
    document.getElementsByName('startDate').forEach((el, _) => {
        el.value = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
    })
}

if (document.getElementById('total_price')) {
    calculateTotalPrice();
}
