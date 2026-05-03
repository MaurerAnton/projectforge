import PropTypes from 'prop-types';
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { clearAllToasts, removeToast } from '../../actions';
import { colorPropType } from '../../utilities/propTypes';
import { Toast, ToastBody, ToastHeader } from '../design';

function Toasts() {
    const toasts = useSelector((state) => state.toasts);
    const dispatch = useDispatch();
    const onClear = () => dispatch(clearAllToasts());
    const onToastRemove = (id) => dispatch(removeToast(id));

    const handleDismissClick = (id) => (event) => {
        if (event.shiftKey) {
            onClear();
        } else {
            onToastRemove(id);
        }
    };

    return (
        <div
            className="p-3 my-2 rounded bg-docs-transparent-grid"
            style={{
                position: 'absolute',
                top: 0,
                right: 0,
            }}
        >
            {toasts
                .filter(({ dismissed }) => dismissed !== true)
                .reverse()
                .slice(0, 3)
                .map((toast) => (
                    <Toast key={`toast-${toast.id}`}>
                        <ToastHeader toggle={handleDismissClick(toast.id)} icon={toast.color}>
                            ProjectForge®
                        </ToastHeader>
                        <ToastBody>{toast.message}</ToastBody>
                    </Toast>
                ))}
        </div>
    );
}

export default Toasts;
