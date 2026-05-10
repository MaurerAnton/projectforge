import {
    baseURL,
    baseRestURL,
    createQueryParams,
    evalServiceURL,
    getServiceURL,
    handleHTTPErrors,
} from './rest';

it('base url', () => {
    expect(baseURL)
        .toBe('');
});

it('base rest url', () => {
    expect(baseRestURL)
        .toBe('/rs');
});

describe('handle HTTP errors', () => {
    it('throws with status code on non-OK response', () => {
        expect(() => handleHTTPErrors({ ok: false, status: 401 }))
            .toThrow('Fetch failed: Error 401');
    });

    it('reports correct status for server errors', () => {
        expect(() => handleHTTPErrors({ ok: false, status: 500 }))
            .toThrow('Fetch failed: Error 500');
    });

    it('returns response unchanged when OK', () => {
        const response = { ok: true, status: 200 };
        expect(handleHTTPErrors(response))
            .toBe(response);
    });
});

describe('create query params', () => {
    it('empty params', () => {
        const params = {};
        const expectedParams = '';

        expect(createQueryParams(params))
            .toBe(expectedParams);
    });

    it('one param', () => {
        const params = {
            amount: 10,
        };
        const expectedParams = 'amount=10';

        expect(createQueryParams(params))
            .toBe(expectedParams);
    });

    it('several params', () => {
        const params = {
            amount: 10,
            flavor: 'sweet',
        };
        const expectedParams = 'amount=10&flavor=sweet';

        expect(createQueryParams(params))
            .toBe(expectedParams);
    });

    it('several params with illegal URI chars', () => {
        const params = {
            amount: 10,
            flavor: 'sweet',
            name: 'Schwarzwälder Kirschtorte',
        };
        const expectedParams = 'amount=10&flavor=sweet&name=Schwarzw%C3%A4lder%20Kirschtorte';

        expect(createQueryParams(params))
            .toBe(expectedParams);
    });
});

describe('eval service url', () => {
    it('returns URL unchanged when no params', () => {
        expect(evalServiceURL('cakes/order'))
            .toBe('cakes/order');
    });

    it('appends query string when params provided', () => {
        expect(evalServiceURL('cakes/order', { id: 1, amount: 123 }))
            .toBe('cakes/order?id=1&amount=123');
    });

    it('uses & when URL already has a query parameter', () => {
        expect(evalServiceURL('cakes/order?page=1', { amount: 10 }))
            .toBe('cakes/order?page=1&amount=10');
    });
});

describe('get service url', () => {
    it('undefined params', () => {
        const serviceURL = 'cakes/order';
        const expectedServiceURL = '/rs/cakes/order';

        expect(getServiceURL(serviceURL))
            .toBe(expectedServiceURL);
    });

    it('empty params', () => {
        const params = {};
        const serviceURL = 'cakes/order';
        const expectedServiceURL = '/rs/cakes/order';

        expect(getServiceURL(serviceURL, params))
            .toBe(expectedServiceURL);
    });

    it('with params', () => {
        const params = {
            id: 1,
            amount: 123,
        };
        const serviceURL = 'cakes/order';
        const expectedServiceURL = '/rs/cakes/order?id=1&amount=123';

        expect(getServiceURL(serviceURL, params))
            .toBe(expectedServiceURL);
    });
});
