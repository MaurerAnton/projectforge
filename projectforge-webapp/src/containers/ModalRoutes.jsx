import React from 'react';
import PropTypes from 'prop-types';
import { useLocation } from 'react-router';
import { Modal, ModalBody } from 'reactstrap';
import { useDispatch } from 'react-redux';
import { callAction } from '../actions';

function ModalRoutes({ getRoutesWithLocation }) {
    const dispatch = useDispatch();
    const onCallAction = (...args) => dispatch(callAction(...args));
    const location = useLocation();
    const realLocation = location.action ? location.location : location;
    const { background } = realLocation.state || {};

    return (
        <>
            {getRoutesWithLocation(background)}
            <Modal
                size="xl"
                isOpen={!!background}
                toggle={() => onCallAction({ responseAction: { targetType: 'CLOSE_MODAL' } })}
            >
                <ModalBody>
                    {background && getRoutesWithLocation(realLocation)}
                </ModalBody>
            </Modal>
        </>
    );
}

ModalRoutes.propTypes = {
    getRoutesWithLocation: PropTypes.func.isRequired,
};

export default ModalRoutes;
