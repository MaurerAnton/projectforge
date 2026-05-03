import classNames from 'classnames';
import PropTypes from 'prop-types';
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addFilter } from '../../../../../actions/list/filter';
import styles from '../../ListPage.module.scss';

function FilterListEntry(
    {
        id,
        label,
        afterSelect,
    },
) {
    const isSelected = useSelector((state) => {
        const listState = state.list;
        return listState.categories[listState.currentCategory].filter.entries
            .filter(({ field }) => field === id).length !== 0;
    });
    const dispatch = useDispatch();
    const onFilterAdd = (filterId) => dispatch(addFilter(filterId));
    const handleSelect = () => {
        if (isSelected) {
            return;
        }

        onFilterAdd(id);
        afterSelect();
    };

    return (
        <li
            className={classNames(styles.filter, { [styles.isSelected]: isSelected })}
            onClick={handleSelect}
            role="option"
            aria-selected="false"
            onKeyPress={undefined}
        >
            {label}
        </li>
    );
}

FilterListEntry.propTypes = {
    id: PropTypes.string.isRequired,
    label: PropTypes.string.isRequired,
    afterSelect: PropTypes.func.isRequired,
};

export default FilterListEntry;
