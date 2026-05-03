import { faFilter, faSearch } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import classNames from 'classnames';
import PropTypes from 'prop-types';
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { resetAllFilters } from '../../../../../actions/list/filter';
import AdvancedPopper from '../../../../../components/design/popper/AdvancedPopper';
import AdvancedPopperAction from '../../../../../components/design/popper/AdvancedPopperAction';
import AdvancedPopperInput from '../../../../../components/design/popper/AdvancedPopperInput';
import { getNamedContainer } from '../../../../../utilities/layout';
import styles from '../../ListPage.module.scss';
import FilterListEntry from './FilterListEntry';
import MagicFilterPill from './MagicFilterPill';

function MagicFilters() {
    const reduxState = useSelector((state) => {
        const listState = state.list;
        const { ui, filter } = listState.categories[listState.currentCategory];
        return {
            translations: ui.translations,
            searchFilter: getNamedContainer('searchFilter', ui.namedContainers),
            filterEntries: filter.entries,
            searchString: filter.searchString,
        };
    });
    const { translations, searchFilter, filterEntries, searchString } = reduxState;
    const dispatch = useDispatch();
    const onResetAllFilters = () => dispatch(resetAllFilters());
    const [allFiltersAreOpen, setAllFiltersAreOpen] = React.useState(false);
    const [search, setSearch] = React.useState('');
    const searchRef = React.useRef(null);

    if (!searchFilter) {
        return null;
    }

    const setIsOpen = (open) => {
        if (searchRef.current) {
            if (open) {
                searchRef.current.focus({ preventScroll: true });
            } else {
                searchRef.current.blur();
            }
        }

        setAllFiltersAreOpen(open);
    };

    const handleSearchChange = ({ target }) => setSearch(target.value);

    const handleAllFiltersDelete = () => {
        setAllFiltersAreOpen(false);
        onResetAllFilters();
    };

    const handleAfterSelectFilter = () => setIsOpen(false);

    const searchLowerCase = search.toLowerCase();
    const filteredSearchFilters = searchFilter && searchFilter.content
        .filter(({ id, label }) => (
            id.toLowerCase()
                .includes(searchLowerCase)
            || label.toLowerCase()
                .includes(searchLowerCase)
        ));

    return (
        <div className={styles.magicFilters}>
            <div className={styles.magicFilter}>
                <AdvancedPopper
                    setIsOpen={setIsOpen}
                    isOpen={allFiltersAreOpen}
                    basic={(
                        <>
                            {`${translations.searchFilter} `}
                            <FontAwesomeIcon icon={faFilter} />
                        </>
                    )}
                    className={styles.allFilters}
                    contentClassName={classNames(
                        styles.pill,
                        { [styles.marked]: allFiltersAreOpen },
                    )}
                    actions={(
                        <AdvancedPopperAction
                            type="delete"
                            disabled={!(filterEntries.length || searchString)}
                            onClick={handleAllFiltersDelete}
                        >
                            {translations.reset || '???Zurücksetzen???'}
                        </AdvancedPopperAction>
                    )}
                >
                    <AdvancedPopperInput
                        forwardRef={searchRef}
                        autoFocus
                        dark
                        id="magicFiltersSearch"
                        icon={faSearch}
                        noStyle
                        onCancel={() => setIsOpen(false)}
                        onChange={handleSearchChange}
                        placeholder={translations.search || ''}
                        selectOnFocus
                        value={search}
                    />
                    <ul className={styles.filterList}>
                        {filteredSearchFilters.map(({ id, label }) => (
                            <FilterListEntry
                                key={`filter-${id}`}
                                afterSelect={handleAfterSelectFilter}
                                id={id}
                                label={label}
                            />
                        ))}
                        {filteredSearchFilters.length === 0 && (
                            <span className={styles.errorMessage}>
                                {translations['datatable.no-records-found']}
                            </span>
                        )}
                    </ul>
                </AdvancedPopper>
            </div>
            {searchFilter.content
                .filter((filter) => filter.defaultFilter)
                .map((filter) => (
                    <MagicFilterPill
                        {...Array.findByField(filterEntries, 'field', filter.id)}
                        {...filter}
                        key={`magic-filter-default-${filter.id}`}
                    />
                ))}
            {filterEntries
                .map((entry) => ({
                    ...Array.findByField(searchFilter.content, 'id', entry.field),
                    ...entry,
                }))
                .filter(({ id, defaultFilter }) => id !== undefined && !defaultFilter)
                .map((entry) => (
                    <MagicFilterPill
                        {...entry}
                        isRemovable
                        key={`magic-filter-${entry.id}`}
                    />
                ))}
        </div>
    );
}

MagicFilters.propTypes = {};

export default MagicFilters;
