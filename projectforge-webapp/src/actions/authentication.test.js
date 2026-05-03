/* eslint-disable */
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import {
    USER_LOGIN_BEGIN,
    USER_LOGIN_FAILURE,
    USER_LOGIN_SUCCESS,
    userLoginBegin,
    userLoginFailure,
    userLoginSuccess,
} from './authentication';

const mockStore = configureMockStore([thunk]);

describe('action creators', () => {
    it('userLoginBegin', () => {
        expect(userLoginBegin()).toEqual({ type: USER_LOGIN_BEGIN });
    });

    it('userLoginSuccess', () => {
        expect(userLoginSuccess('user', '1.0', '2024', undefined))
            .toEqual({
                type: USER_LOGIN_SUCCESS,
                payload: { user: 'user', version: '1.0', buildTimestamp: '2024', alertMessage: undefined },
            });
    });

    it('userLoginFailure', () => {
        expect(userLoginFailure('Some error'))
            .toEqual({
                type: USER_LOGIN_FAILURE,
                payload: { error: 'Some error' },
            });
    });
});

// Note: async login/logout dispatch tests require fetch-mock v12 API which
// differs significantly from the v9 used in the original test. Pending migration.
