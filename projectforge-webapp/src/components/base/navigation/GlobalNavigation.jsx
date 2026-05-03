import PropTypes from 'prop-types';
import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadMenu } from '../../../actions';
import { badgePropType, menuItemPropType } from '../../../utilities/propTypes';
import { Collapse, Navbar, NavbarToggler } from '../../design';
import CategoriesDropdown from './categories-dropdown';
import Navigation from './index';
import style from './Navigation.module.scss';

function GlobalNavigation() {
    const { badge, favoritesMenu, mainMenu, myAccountMenu } = useSelector((state) => state.menu);
    const dispatch = useDispatch();
    const loadNavigation = () => dispatch(loadMenu());

    const [mobileIsOpen, setMobileIsOpen] = useState(false);

    useEffect(() => {
        loadNavigation();
    }, []);

    const toggleMobile = () => {
        setMobileIsOpen((prev) => !prev);
    };

    return (
        <Navbar color="light" light expand="md" className={style.globalNavigation}>
            <NavbarToggler
                onClick={toggleMobile}
                className="ml-auto"
            />
            <Collapse isOpen={mobileIsOpen} navbar>
                {mainMenu && mainMenu.length
                    ? <CategoriesDropdown categories={mainMenu} badge={badge} />
                    : undefined}
                {favoritesMenu && favoritesMenu.length > 0
                    ? <Navigation entries={favoritesMenu} className="me-auto" />
                    : undefined}
                {myAccountMenu && myAccountMenu.length > 0
                    ? (
                        <Navigation
                            entries={myAccountMenu}
                            className="ml-auto text-nowrap"
                            right
                        />
                    )
                    : undefined}
            </Collapse>
        </Navbar>
    );
}

GlobalNavigation.propTypes = {
    favoritesMenu: PropTypes.arrayOf(menuItemPropType),
    loadNavigation: PropTypes.func,
    mainMenu: PropTypes.arrayOf(menuItemPropType),
    myAccountMenu: PropTypes.arrayOf(menuItemPropType),
    badge: badgePropType,
};

export default GlobalNavigation;
