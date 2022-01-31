const reducer = Redux.combineReducers({
    todos: (state = [], action = {}) => {
        const newState = Object.assign([], state);
        if (action.type === 'add') {
            newState.push(action.item);
        }
        if(action.type === 'remove') {
            newState.splice(action.index, 1);
        }
        return newState;
    }
});

const store = Redux.createStore(reducer);

const render = () => {
    const list = document.getElementById('list');
    list.innerHTML = '';
    const state = store.getState();
    state.todos.forEach((todo, index) => {
        const item = document.createElement('li');
        item.innerHTML = todo;
        list.appendChild(item);
        item.onclick = (e) => {
            store.dispatch({
                type: 'remove',
                index: index
            });
            render();
        }
    })
}

render();

document.getElementById('submit-todo').onclick = () => {
    store.dispatch({
        type: 'add',
        item: document.getElementById('todo-item').value
    });
    document.getElementById('todo-item').value = '';
    render();
};