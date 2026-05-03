import PropTypes from 'prop-types';
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { useSelector, useDispatch } from 'react-redux';
import { sortList } from '../../../../../actions/list/filter';
import AnimatedChevron from '../../../../design/input/chevron/Animated';
import style from './DynamicTable.module.scss';

function DynamicListPageTableHead(
    {
        id,
        sortable = false,
        title,
        titleIcon,
    },
) {
    const direction = useSelector((state) => {
        const listState = state.list;
        const currentCategory = listState.categories[listState.currentCategory];
        if (!currentCategory) return undefined;
        return (Array.findByField(
            currentCategory.filter.sortProperties,
            'property',
            id,
        ) || {}).sortOrder;
    });
    const dispatch = useDispatch();
    const dispatchSort = (...args) => dispatch(sortList(...args));

    const handleHeadClick = () => {
        if (sortable) {
            dispatchSort(id, direction);
        }
    };

    const head = titleIcon ? <FontAwesomeIcon icon={titleIcon} /> : title;

    return (
        <th onClick={handleHeadClick} className={sortable ? style.clickableTableHead : ''}>
            {head}
            {sortable && <AnimatedChevron direction={direction} />}
        </th>
    );
}

DynamicListPageTableHead.propTypes = {
    id: PropTypes.string.isRequired,
    title: PropTypes.string,
    titleIcon: PropTypes.arrayOf(PropTypes.string),
    sortable: PropTypes.bool,
};

export default DynamicListPageTableHead;
