import PropTypes from 'prop-types';
import React from 'react';
import { useSelector } from 'react-redux';
import moment from 'moment';
import { Button } from '../../../../../design';
import { DynamicLayoutContext } from '../../../context';

function CustomizedBookLendOutComponent() {
    const user = useSelector((state) => state.authentication.user);
    const jsTimestampFormatMinutes = useSelector((state) => state.authentication.user.jsTimestampFormatMinutes);
    const { data, ui, callAction } = React.useContext(DynamicLayoutContext);

    const lendOut = () => callAction({
        responseAction: {
            url: 'book/lendOut',
            targetType: 'POST',
        },
    });
    const handBack = () => callAction({
        responseAction: {
            url: 'book/returnBook',
            targetType: 'POST',
        },
    });

    return React.useMemo(
        () => (
            <>
                {data.lendOutBy && data.lendOutDate
                    ? (
                        <>
                            <span className="mr-4">
                                {`${data.lendOutBy.displayName}, ${moment(data.lendOutDate).format(jsTimestampFormatMinutes)}`}
                            </span>
                            {user.username === data.lendOutBy.username
                                ? (
                                    <Button color="danger" outline onClick={handBack}>
                                        {ui.translations['book.returnBook']}
                                    </Button>
                                )
                                : undefined}
                        </>
                    )
                    : undefined}
                <Button color="link" onClick={lendOut}>
                    {ui.translations['book.lendOut']}
                </Button>
            </>
        ),
        [data.lendOutBy, data.lendOutDate],
    );
}

CustomizedBookLendOutComponent.propTypes = {};

export default CustomizedBookLendOutComponent;
