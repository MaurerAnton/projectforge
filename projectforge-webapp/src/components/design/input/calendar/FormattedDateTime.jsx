import moment from 'moment';
import PropTypes from 'prop-types';
import React from 'react';
import { useSelector } from 'react-redux';

function FormattedDateTime(
    {
        date,
        slot = 'FROM',
        ...props
    },
) {
    const jsDateFormat = useSelector((state) => state.authentication.user.jsDateFormat);
    const jsTimestampFormatMinutes = useSelector((state) => state.authentication.user.jsTimestampFormatMinutes);
    let format = jsTimestampFormatMinutes;

    if (
        (slot === 'FROM' && date.getHours() === 0 && date.getMinutes() === 0)
        || (slot === 'TO' && date.getHours() === 23 && date.getMinutes() === 59)) {
        format = jsDateFormat;
    }

    return (
        <span {...props}>
            {moment(date)
                .format(format)}
        </span>
    );
}

FormattedDateTime.propTypes = {
    date: PropTypes.instanceOf(Date).isRequired,
    slot: PropTypes.oneOf(['FROM', 'TO']),
};

export default FormattedDateTime;
