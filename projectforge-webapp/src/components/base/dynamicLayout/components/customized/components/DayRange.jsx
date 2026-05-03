import timezone from 'moment-timezone';
import 'moment/min/locales';
import PropTypes from 'prop-types';
import 'rc-time-picker/assets/index.css';
import React from 'react';
import 'react-day-picker/src/style.css';
import { useSelector } from 'react-redux';
import AdditionalLabel from '../../../../../design/input/AdditionalLabel';
import TimeRange from '../../../../../design/input/calendar/TimeRange';
import { DynamicLayoutContext } from '../../../context';

/**
 * Range of day for time sheets.
 */
function DayRange(
    {
        additionalLabel,
        id,
        values,
    },
) {
    const dateFormat = useSelector((state) => state.authentication.user.jsDateFormat);
    const locale = useSelector((state) => state.authentication.user.locale);
    const timeNotation = useSelector((state) => state.authentication.user.timeNotation);
    const { data, setData, ui } = React.useContext(DynamicLayoutContext);
    const { startDateId, endDateId, label } = values;

    const resolveDate = (dateId) => {
        const dateEpochSeconds = Object.getByString(data, dateId);
        return dateEpochSeconds ? timezone(new Date(dateEpochSeconds)) : undefined;
    };

    const [startDate, setStartDate] = React.useState(undefined);
    const [endDate, setEndDate] = React.useState(undefined);

    React.useEffect(() => {
        setStartDate(resolveDate(startDateId));
    }, [Object.getByString(data, startDateId)]);

    React.useEffect(() => {
        setEndDate(resolveDate(endDateId));
    }, [Object.getByString(data, endDateId)]);

    return React.useMemo(() => {
        const setFields = (newStartDate, newEndDate) => {
            newEndDate.set({
                year: newStartDate.year(),
                dayOfYear: newStartDate.dayOfYear(),
                second: 0,
                millisecond: 0,
            });

            const endDayTime = newEndDate.hours() * 60 + newEndDate.minutes();
            const startDayTime = newStartDate.hours() * 60 + newStartDate.minutes();

            if (endDayTime < startDayTime) {
                // Assume next day for endDate.
                newEndDate.add(1, 'days');
            }

            setData({
                [startDateId]: newStartDate.toDate(),
                [endDateId]: newEndDate.toDate(),
            });
        };

        const changeStartTime = (value) => setFields(timezone(value), endDate);
        const changeEndTime = (value) => setFields(startDate, timezone(value));

        return (
            <>
                <TimeRange
                    label={label}
                    from={startDate ? startDate.toDate() : undefined}
                    id={`${ui.uid}-${id}`}
                    sameDate
                    setFrom={changeStartTime}
                    setTo={changeEndTime}
                    to={endDate ? endDate.toDate() : undefined}
                    toLabel={ui.translations.until}
                />
                <AdditionalLabel title={additionalLabel} />
            </>
        );
    }, [startDate, endDate, setData]);
}

DayRange.propTypes = {
    values: PropTypes.shape({
        startDateId: PropTypes.string,
        endDateId: PropTypes.string,
        label: PropTypes.string,
    }).isRequired,
    additionalLabel: PropTypes.string,
    id: PropTypes.string,
};

export default DayRange;
