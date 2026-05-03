import React from 'react';
import { createRoot } from 'react-dom/client';
import ProjectForge from './ProjectForge';

describe('renders without crashing', () => {
    it('with initial state', () => {
        const div = document.createElement('div');

        createRoot(div).render(
            <ProjectForge loginInProgress user={null} loadUserStatus={() => {}} />,
        );
    });

    it('with logged in state', () => {
        const div = document.createElement('div');

        createRoot(div).render(
            <ProjectForge loginInProgress={false} user={{ name: 'test' }} loadUserStatus={() => {}} />,
        );
    });
});
