import { faSearch, faSync } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import classNames from 'classnames';
import PropTypes from 'prop-types';
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Button, Navbar } from 'reactstrap';
import { useNavigate, useLocation } from 'react-router';
import {
    createListFavorite,
    deleteListFavorite,
    dismissCurrentError,
    fetchCurrentList,
    exportCurrentList,
    startMultiSelection,
    renameListFavorite,
    selectListFavorite,
    updateListFavorite,
} from '../../../../actions';
import { changeSearchString } from '../../../../actions/list/filter';
import Navigation from '../../../../components/base/navigation';
import { Alert, Col, Spinner } from '../../../../components/design';
import TextAutoCompletion
    from '../../../../components/design/input/autoCompletion/TextAutoCompletion';
import AdvancedPopperAction from '../../../../components/design/popper/AdvancedPopperAction';
import FavoritesPanel from '../../../panel/favorite/FavoritesPanel';
import styles from '../ListPage.module.scss';
import MagicFilters from './magicFilter/MagicFilters';

function SearchFilter() {
    const category = useSelector((state) => {
        const listState = state.list;
        return listState.categories[listState.currentCategory];
    });
    const dispatch = useDispatch();
    const onErrorDismiss = () => dispatch(dismissCurrentError());
    const onFavoriteCreate = (name) => dispatch(createListFavorite({ name }));
    const onFavoriteDelete = (id) => dispatch(deleteListFavorite({ id }));
    const onFavoriteRename = (id, newName) => dispatch(renameListFavorite({ id, newName }));
    const onFavoriteSelect = (id) => dispatch(selectListFavorite({ id }));
    const onFavoriteUpdate = () => dispatch(updateListFavorite());
    const onSearchStringBlur = () => dispatch(fetchCurrentList());
    const onSearchStringChange = (completion) => dispatch(changeSearchString(completion));
    const onSearchStringDelete = () => dispatch(changeSearchString(''));
    const onSyncButtonClick = () => dispatch(fetchCurrentList(true));
    const onExportButtonClick = () => dispatch(exportCurrentList());
    const onMultiSelectionButtonClick = () => dispatch(startMultiSelection());

    const {
        error,
        filter,
        filterFavorites,
        isFetching,
        newlySwitched,
        quickSelectUrl,
        standardEditPage,
        ui,
        useModalEditDialog,
    } = category;

    const navigate = useNavigate();
    const location = useLocation();

    const onSelectQuickSelection = ({ id }) => {
        let url = `/${standardEditPage.replace(':id', id)}`;

        if (useModalEditDialog) {
            // Add modal=true query parameter so backend knows it was opened in modal context
            url += url.includes('?') ? '&modal=true' : '?modal=true';
            navigate(url, { state: { background: location } });
        } else {
            navigate(url);
        }
    };

    return (
        <>
            <div className={styles.searchRow}>
                {/* FLEX-BOX IS SET TO REVERSE ON BIG SCREENS */}
                <div className={classNames(styles.container, styles.flex)}>
                    {/* Render the menu if it's loaded. */}
                    {ui && ui.pageMenu && (
                        <Col>
                            <Navbar>
                                <Navigation
                                    entries={ui.pageMenu}
                                    // Let the menu float to the right.
                                    className="ml-auto"
                                />
                            </Navbar>
                        </Col>
                    )}
                </div>
                <div className={styles.container}>
                    <FavoritesPanel
                        onFavoriteCreate={onFavoriteCreate}
                        onFavoriteDelete={onFavoriteDelete}
                        onFavoriteRename={onFavoriteRename}
                        onFavoriteSelect={onFavoriteSelect}
                        onFavoriteUpdate={onFavoriteUpdate}
                        favorites={filterFavorites}
                        currentFavoriteId={filter.id}
                        isModified
                        closeOnSelect={false}
                        translations={ui.translations}
                        htmlId="searchFilterFavoritesPopover"
                        newFavoriteI18nKey="favorite.filter.addNew"
                    />
                    {ui && ui.excelExportSupported && (
                        <Button
                            id="excelExport"
                            color="primary"
                            onClick={onExportButtonClick}
                            outline
                        >
                            {ui.translations.exportAsXls}
                        </Button>
                    )}
                    {ui && ui.multiSelectionSupported && (
                        <Button
                            id="multiSelection"
                            color="primary"
                            onClick={onMultiSelectionButtonClick}
                            outline
                        >
                            {/* eslint-disable-next-line react/prop-types */}
                            {ui.translations['multiselection.button']}
                        </Button>
                    )}
                    {isFetching && <Spinner className={styles.loadingSpinner} />}
                </div>
                <TextAutoCompletion
                    actions={(
                        <AdvancedPopperAction
                            type="delete"
                            disabled={!filter.searchString}
                            onClick={onSearchStringDelete}
                        >
                            {ui.translations.delete || ''}
                        </AdvancedPopperAction>
                    )}
                    className={styles.searchContainer}
                    inputId="searchString"
                    inputProps={{
                        autoFocus: newlySwitched,
                        icon: faSearch,
                        noStyle: true,
                        onBlur: onSearchStringBlur,
                        placeholder: ui.translations.search || '',
                        selectOnFocus: newlySwitched,
                        children: (
                            <FontAwesomeIcon
                                icon={faSync}
                                className={styles.syncButton}
                                onClick={onSyncButtonClick}
                            />
                        ),
                    }}
                    onChange={onSearchStringChange}
                    onSelect={onSelectQuickSelection}
                    url={quickSelectUrl}
                    value={filter.searchString}
                    withInput={false}
                />
            </div>
            <MagicFilters />
            <hr />
            <Alert
                color="danger"
                className={styles.alert}
                toggle={onErrorDismiss}
                isOpen={error !== undefined}
                fade
                timeout={150}
            >
                <h4>Oh Snap!</h4>
                <p>Error while contacting the server. Please contact an administrator.</p>
            </Alert>
        </>
    );
}

SearchFilter.propTypes = {};

export default SearchFilter;
