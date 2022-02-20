element = document.getElementById('ingredients');
const choices = new Choices(element, {
    silent: true,
    searchEnabled: true,
    shouldSort: false,
    placeholder: true,
    allowDuplicates: false,
    maxItemCount: 5,
    removeItems: true,
    maxItemText: "Это максимальное количество"
    }
);