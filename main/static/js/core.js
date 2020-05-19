const body = document.getElementById('body_table');

document.querySelectorAll('.delete_button').forEach(button=>button.addEventListener('click',delFunction))

function  addBlockRow(row) {
row.classList.add('is_done_text');
}

function  removeBlockRow(row) {
row.classList.remove('is_done_text');
}


function createMessageBlock(title, text) {
    const divBlock = document.createElement('div');
    divBlock.className = 'wrapper__auth';
    divBlock.id = "id_new_edit_block";
    divBlock.innerHTML = `<div class="auth__column_right_delete"><div class="auth__column_right_delete_down"><div class="auth__column_right_form__header">${title}</div><div id="message_text" class="auth__column_right_form__text"> ${text}</div><div class="auth__column_right__form_footer"><label class="form_footer_button-submit"><input type="submit" form="auth_form" value="" style="display: none"><a href="#" id="login-submit-btn"><div class="auth__button_submit"  ><span>&#10004</span></div></a></label><label class="form_footer_button-cancel"><a href="#" id="cancel_btn"><div class="auth__button_submit" id="login-cancel-btn" ><span>&#9587</span></div></a></label></div></div></div>`;
    return divBlock;
}

function createEmptyTableRow() {
    const emptyRow = document.createElement('div');
    emptyRow.className = 'table-data__table-row';
    emptyRow.innerHTML = `<div class="table-row_table_cell-1"></div>`;
    return emptyRow;
}

function deleteMessageBlock(event) {
    event.preventDefault();
    document.getElementById('id_new_edit_block').remove();
}

function delFunction(event) {
event.preventDefault();
const url = event.currentTarget.href;
const message = createMessageBlock('Alert!', 'Do you want delete this task?');
body.appendChild(message);
document.getElementById("login-cancel-btn").addEventListener(
    'click', event=>deleteMessageBlock(event));
document.getElementById("login-submit-btn").addEventListener(
    'click', event=>deleteRecord(url, event));
}
