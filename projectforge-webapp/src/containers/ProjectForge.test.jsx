import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { thunk } from 'redux-thunk';
import { MemoryRouter } from 'react-router';

vi.mock('../components/base/footer', () => ({ default: () => null }));
vi.mock('../components/base/Toasts', () => ({ default: () => null }));
vi.mock('../components/base/topbar', () => ({ default: () => null }));
vi.mock('../components/base/navigation/GlobalNavigation', () => ({ default: () => null }));
vi.mock('../components/design', () => ({ default: {}, Spinner: () => null }));
vi.mock('./AuthorizedRoutes', () => ({ default: () => null, publicRoute: null, wicketRoute: null }));
vi.mock('./page/form/FormPage', () => ({ default: () => null }));

const mockFetchResponse = Promise.resolve({
    ok: true,
    json: () => Promise.resolve({}),
});

global.fetch = vi.fn(() => mockFetchResponse);

import ProjectForge from './ProjectForge';

function createTestStore(initialState) {
    const rootReducer = (state = initialState) => state;
    return createStore(rootReducer, initialState, applyMiddleware(thunk));
}

describe('renders without crashing', () => {
    it('with initial state', () => {
        const store = createTestStore({
            authentication: { loading: true, user: null },
        });
        const div = document.createElement('div');

        createRoot(div).render(
            <Provider store={store}>
                <MemoryRouter>
                    <ProjectForge />
                </MemoryRouter>
            </Provider>,
        );
    });

    it('with logged in state', () => {
        const store = createTestStore({
            authentication: { loading: false, user: { name: 'test' } },
        });
        const div = document.createElement('div');

        createRoot(div).render(
            <Provider store={store}>
                <MemoryRouter>
                    <ProjectForge />
                </MemoryRouter>
            </Provider>,
        );
    });
});
