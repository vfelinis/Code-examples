<div data-bind="if: viewModel.updateStatus">
	<div data-bind='component:
		{ name: "update-component", params: viewModel.updateDoc }'></div>
</div>
<div data-bind="ifnot: viewModel.updateStatus">
	<h1 data-bind="text: viewModel.title"></h1>

	<div data-bind="if: viewModel.visible">
		<form id="addForm" enctype="multipart/form-data" class="form-horizontal" role="form">
			<div class="form-group">
				<label for="doc_file" class="col-sm-2 control-label">Файл</label>
				<div class="col-sm-10">
					<input type="file" class="form-control" id="doc_file" name="doc_file">
				</div>
			</div>
			<div class="form-group">
				<label for="doc_text" class="col-sm-2 control-label">Описание</label>
				<div class="col-sm-10">
					<input type="text" class="form-control" id="doc_text" name="doc_text">
				</div>
			</div>
			<div class="form-group">
				<label for="doc_date" class="col-sm-2 control-label">Дата</label>
				<div class="col-sm-3">
					<input type="date" class="form-control" id="doc_date" name="doc_date">
				</div>
			</div>
			<div class="form-group">
				<div class="col-sm-offset-2 col-sm-2">
					<button type="submit" class="btn btn-default">
						Создать
					</button>
				</div>
				<div class="col-sm-2">
					<button class="btn btn-default" data-bind="click: cancel">
						Отмена
					</button>
				</div>
			</div>
		</form>
	</div>

	<div data-bind="ifnot: viewModel.visible">
		<button class="btn btn-default btn-lg" data-bind="click: addVisible">
			Добавить новый документ
		</button>
		<div class="navbar-form navbar-right">
			<input type="text" class="form-control" placeholder="Поиск" data-bind="value: viewModel.search, valueUpdate: 'afterkeydown'">
		</div>
		<table class="table table-striped">
			<thead>
				<tr>
					<th>Файл</th>
					<th>Описание</th>
					<th>Дата</th>
					<th></th>
					<th></th>
				</tr>
			</thead>
			<tbody data-bind="foreach: viewModel.filteredDocuments">
				<tr>
					<td>
						<a data-bind="attr: { href: '/core/getFile.php?file_id='+file.$id }, text: fileName"></a>
					</td>
					<td data-bind="text: text"></td>
					<td data-bind="text: date"></td>
					<td>
						<button class="btn btn-xs btn-primary" data-bind="click: update">
		                    Изменить
		                </button>
					</td>
					<td>
						<button class="btn btn-xs btn-primary" data-bind="click: remove">
		                    Удалить
		                </button>
					</td>
				</tr>
			</tbody>
		</table>
		<div style="text-align: center;">
			<ul class="pagination" data-bind="foreach: viewModel.pages">
				<li data-bind="css: { active: $data == viewModel.page() }"><a style="cursor: pointer;" data-bind="text: $data, click: index"></a></li>
			</ul>
		</div>
	</div>
<div>