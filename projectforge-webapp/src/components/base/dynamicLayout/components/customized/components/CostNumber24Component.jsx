import React from 'react';
import { useSelector } from 'react-redux';
import { DynamicLayoutContext } from '../../../context';

function CostNumber24Component() {
    const user = useSelector((state) => state.authentication.user);
    const jsTimestampFormatMinutes = useSelector((state) => state.authentication.user.jsTimestampFormatMinutes);
    const { data, setData } = React.useContext(DynamicLayoutContext);

    const handleBereichChange = (event) => {
        // console.log(event.target.value)
        setData({ bereich: event.target.value });
    };

    const handleNummerChange = (event) => {
        // console.log(event.target.value)
        setData({ nummer: event.target.value });
    };

    function ensureBereich() {
        if (data.bereich === undefined) {
            return '0';
        }
        return data.bereich.toString();
    }

    return React.useMemo(
        () => (
            <>
                Projektnummer
                <br />
                {data.nummernkreis}
                .
                <input
                    id="bereich"
                    type="number"
                    size="3"
                    min="0"
                    max="999"
                    value={ensureBereich}
                    onChange={handleBereichChange}
                />
                .
                <input
                    id="nummer"
                    type="number"
                    size="2"
                    min="0"
                    max="99"
                    value={data.nummer.toString()}
                    onChange={handleNummerChange}
                />
                .
                ##
            </>
        ),
    );
}

export default CostNumber24Component;
