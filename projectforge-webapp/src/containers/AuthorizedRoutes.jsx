import React, { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { Route, Routes } from 'react-router';
import GlobalNavigation from '../components/base/navigation/GlobalNavigation';
import { Alert, Container } from '../components/design';
import prefix from '../utilities/prefix';
import CalendarPage from './page/calendar/CalendarPage';
import FormPage from './page/form/FormPage';
import IndexPage from './page/IndexPage';
import ListPage from './page/list/ListPage';
import TaskTreePage from './page/TaskTreePage';
import ModalRoutes from './ModalRoutes';
import RedirectToWicket from './RedirectToWicket';
import FormModal from './page/form/FormModal';
import MenuCustomizerPanel from './panel/menu/MenuCustomizerPanel';

export const wicketRoute = (
    <Route
        path="/wa/*"
        element={<RedirectToWicket />}
    />
);

export const publicRoute = (
    <Route
        path={`${prefix}public/:category/:type?/:id?/:tab?`}
        element={<FormPage isPublic />}
    />
);

function AuthorizedRoutes() {
    const alertMessage = useSelector((state) => state.authentication.alertMessage);
    const locale = useSelector((state) => state.authentication.user?.locale) || 'en';

    useEffect(() => {
        document.documentElement.lang = locale;
    }, [locale]);

    const getRoutesWithLocation = (location) => (
        <Routes location={location}>
            {wicketRoute}
            {publicRoute}
            <Route
                exact
                path={prefix}
                element={<IndexPage />}
            />
            <Route
                path={`${prefix}calendar`}
                element={<CalendarPage />}
            >
                <Route
                    path={`${prefix}calendar/:category/:type/:id?/:tab?`}
                    element={<FormModal />}
                />
            </Route>
            <Route
                path={`${prefix}taskTree`}
                element={<TaskTreePage />}
            />
            <Route
                path={`${prefix}customizeMenu`}
                element={<MenuCustomizerPanel />}
            />
            <Route
                path={`${prefix}:category/:type/:id?/:tab?`}
                element={<FormPage />}
            />
            <Route
                path={`${prefix}:category`}
                element={<ListPage />}
            />
        </Routes>
    );

    return (
        <>
            <GlobalNavigation />
            {alertMessage ? (
                <Container fluid>
                    <Alert color="danger">
                        {alertMessage}
                    </Alert>
                </Container>
            ) : undefined}
            <ModalRoutes getRoutesWithLocation={getRoutesWithLocation} />
        </>
    );
}

export default AuthorizedRoutes;
