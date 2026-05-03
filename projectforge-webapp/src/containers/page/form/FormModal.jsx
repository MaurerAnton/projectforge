import PropTypes from 'prop-types';
import React from 'react';
import { useDispatch } from 'react-redux';
import { Modal, ModalBody } from '../../../components/design';
import FormPage from './FormPage';
import { callAction } from '../../../actions';

function FormModal(props) {
    const dispatch = useDispatch();
    const onCallAction = (...args) => dispatch(callAction(...args));

    return (
        <Modal
            toggle={() => onCallAction({ responseAction: { targetType: 'CLOSE_MODAL' } })}
            isOpen
            className="modal-xl"
        >
            <ModalBody>
                <FormPage {...props} />
            </ModalBody>
        </Modal>
    );
}

FormModal.propTypes = {};

export default FormModal;
